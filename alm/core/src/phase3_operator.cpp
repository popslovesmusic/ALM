#include "alm/core/phase3_operator.hpp"

#include <immintrin.h>

namespace {
constexpr int kLaneOffsetsEven[8] = {0, 2, 4, 6, 8, 10, 12, 14};
constexpr int kLaneOffsetsOdd[8] = {1, 3, 5, 7, 9, 11, 13, 15};
constexpr int kLaneOffsetsEvenHigh[8] = {16, 18, 20, 22, 24, 26, 28, 30};
constexpr int kLaneOffsetsOddHigh[8] = {17, 19, 21, 23, 25, 27, 29, 31};
}

Phase3Operator::Phase3Operator(TimeStencil& stencil) : stencil_(&stencil) {}

Phase3Metrics Phase3Operator::tick() {
    auto* now = stencil_->now_slice();
    auto* future = stencil_->future_slice();
    const auto* recent = stencil_->recent_slice();

#if defined(__AVX2__)
    Phase3Metrics metrics = tick_avx2(now, recent, future);
#else
    Phase3Metrics metrics = tick_scalar(now, recent, future);
#endif

    metrics_log_.push_back(metrics);
    return metrics;
}

Phase3Metrics Phase3Operator::tick_scalar(TimeStencil::Value* now,
                                          const TimeStencil::Value* recent,
                                          TimeStencil::Value* future) {
    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;
    Phase3Metrics metrics{};
    metrics.lane_pairs_processed = TensorCluster::kCells * TensorCluster::kRegisters *
                                   (TensorCluster::kSimdLanes / 2);

    float residual_energy = 0.0F;
    float persistence = 0.0F;
    float symmetry = 0.0F;
    float diffusion = 0.0F;
    float sum_out = 0.0F;
    float sumsq_out = 0.0F;

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        const std::size_t neighbor_base = ((cell + 1) % TensorCluster::kCells) * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t reg_offset = base + reg * register_span;
            const std::size_t neighbor_offset = neighbor_base + reg * register_span;
            for (std::size_t pair = 0; pair < TensorCluster::kSimdLanes / 2; ++pair) {
                const std::size_t even_index = reg_offset + pair * 2;
                const std::size_t odd_index = even_index + 1;

                const auto even = now[even_index];
                const auto odd = now[odd_index];
                const auto neighbor_even = now[neighbor_offset + pair * 2];
                const auto neighbor_odd = now[neighbor_offset + pair * 2 + 1];
                const auto residual = even - odd;
                const auto neighbor_residual = neighbor_even - neighbor_odd;
                const auto diffused = residual + neighbor_residual;

                const auto even_out = even + diffused;
                const auto odd_out = odd - diffused;

                future[even_index] = even_out;
                future[odd_index] = odd_out;

                const auto previous_residual = recent[even_index] - recent[odd_index];
                const auto delta_residual = residual - previous_residual;

                residual_energy += residual * residual;
                persistence += delta_residual * delta_residual;
                const auto pair_sum = even_out + odd_out;
                symmetry += pair_sum * pair_sum;
                const auto spread = residual - neighbor_residual;
                diffusion += spread * spread;

                sum_out += even_out + odd_out;
                sumsq_out += even_out * even_out + odd_out * odd_out;
            }
        }
    }

    const float total_values = static_cast<float>(TensorCluster::kCells *
                                                  TensorCluster::kRegisters *
                                                  TensorCluster::kSimdLanes);
    const float inv_total = 1.0F / total_values;
    const float mean_out = sum_out * inv_total;
    const float mean_sq = sumsq_out * inv_total;

    metrics.residual_energy = residual_energy;
    metrics.residual_persistence = persistence;
    metrics.pair_symmetry_drift = symmetry;
    metrics.diffusion_spread = diffusion;
    metrics.output_variance = mean_sq - mean_out * mean_out;

    return metrics;
}

#if defined(__AVX2__)
Phase3Metrics Phase3Operator::tick_avx2(TimeStencil::Value* now,
                                        const TimeStencil::Value* recent,
                                        TimeStencil::Value* future) {
    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;

    Phase3Metrics metrics{};
    metrics.lane_pairs_processed = TensorCluster::kCells * TensorCluster::kRegisters *
                                   (TensorCluster::kSimdLanes / 2);

    __m256 residual_energy = _mm256_setzero_ps();
    __m256 persistence = _mm256_setzero_ps();
    __m256 symmetry = _mm256_setzero_ps();
    __m256 diffusion = _mm256_setzero_ps();
    __m256 sum_out = _mm256_setzero_ps();
    __m256 sumsq_out = _mm256_setzero_ps();

    const __m256i idx_even = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(kLaneOffsetsEven));
    const __m256i idx_odd = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(kLaneOffsetsOdd));
    const __m256i idx_even_high =
        _mm256_loadu_si256(reinterpret_cast<const __m256i*>(kLaneOffsetsEvenHigh));
    const __m256i idx_odd_high =
        _mm256_loadu_si256(reinterpret_cast<const __m256i*>(kLaneOffsetsOddHigh));

    alignas(32) float even_buffer[8];
    alignas(32) float odd_buffer[8];

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        const std::size_t neighbor_base = ((cell + 1) % TensorCluster::kCells) * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t reg_offset = base + reg * register_span;
            const std::size_t neighbor_offset = neighbor_base + reg * register_span;

            auto process_half = [&](const __m256i& even_idx, const __m256i& odd_idx,
                                    std::size_t offset) {
                const auto* now_base = now + reg_offset + offset;
                const auto* recent_base = recent + reg_offset + offset;
                const auto* neighbor_base_ptr = now + neighbor_offset + offset;
                auto* future_base = future + reg_offset + offset;

                const __m256 even = _mm256_i32gather_ps(now_base, even_idx, sizeof(float));
                const __m256 odd = _mm256_i32gather_ps(now_base, odd_idx, sizeof(float));
                const __m256 neighbor_even =
                    _mm256_i32gather_ps(neighbor_base_ptr, even_idx, sizeof(float));
                const __m256 neighbor_odd =
                    _mm256_i32gather_ps(neighbor_base_ptr, odd_idx, sizeof(float));

                const __m256 residual = _mm256_sub_ps(even, odd);
                const __m256 neighbor_residual = _mm256_sub_ps(neighbor_even, neighbor_odd);
                const __m256 diffused = _mm256_add_ps(residual, neighbor_residual);

                const __m256 even_out = _mm256_add_ps(even, diffused);
                const __m256 odd_out = _mm256_sub_ps(odd, diffused);

                _mm256_store_ps(even_buffer, even_out);
                _mm256_store_ps(odd_buffer, odd_out);

                for (int lane = 0; lane < 8; ++lane) {
                    future_base[kLaneOffsetsEven[lane]] = even_buffer[lane];
                    future_base[kLaneOffsetsOdd[lane]] = odd_buffer[lane];
                }

                const __m256 previous_even =
                    _mm256_i32gather_ps(recent_base, even_idx, sizeof(float));
                const __m256 previous_odd =
                    _mm256_i32gather_ps(recent_base, odd_idx, sizeof(float));
                const __m256 previous_residual = _mm256_sub_ps(previous_even, previous_odd);
                const __m256 delta_residual = _mm256_sub_ps(residual, previous_residual);

                residual_energy =
                    _mm256_add_ps(residual_energy, _mm256_mul_ps(residual, residual));
                persistence =
                    _mm256_add_ps(persistence, _mm256_mul_ps(delta_residual, delta_residual));

                const __m256 pair_sum = _mm256_add_ps(even_out, odd_out);
                symmetry = _mm256_add_ps(symmetry, _mm256_mul_ps(pair_sum, pair_sum));

                const __m256 spread = _mm256_sub_ps(residual, neighbor_residual);
                diffusion = _mm256_add_ps(diffusion, _mm256_mul_ps(spread, spread));

                sum_out = _mm256_add_ps(sum_out, _mm256_add_ps(even_out, odd_out));
                sumsq_out = _mm256_add_ps(sumsq_out, _mm256_mul_ps(even_out, even_out));
                sumsq_out = _mm256_add_ps(sumsq_out, _mm256_mul_ps(odd_out, odd_out));
            };

            process_half(idx_even, idx_odd, 0);
            process_half(idx_even_high, idx_odd_high, 16);
        }
    }

    alignas(32) float buffer[8];

    _mm256_store_ps(buffer, residual_energy);
    float residual_energy_total = 0.0F;
    for (float v : buffer) residual_energy_total += v;

    _mm256_store_ps(buffer, persistence);
    float persistence_total = 0.0F;
    for (float v : buffer) persistence_total += v;

    _mm256_store_ps(buffer, symmetry);
    float symmetry_total = 0.0F;
    for (float v : buffer) symmetry_total += v;

    _mm256_store_ps(buffer, diffusion);
    float diffusion_total = 0.0F;
    for (float v : buffer) diffusion_total += v;

    _mm256_store_ps(buffer, sum_out);
    float sum_out_total = 0.0F;
    for (float v : buffer) sum_out_total += v;

    _mm256_store_ps(buffer, sumsq_out);
    float sumsq_out_total = 0.0F;
    for (float v : buffer) sumsq_out_total += v;

    const float total_values = static_cast<float>(TensorCluster::kCells *
                                                  TensorCluster::kRegisters *
                                                  TensorCluster::kSimdLanes);
    const float inv_total = 1.0F / total_values;
    const float mean_out = sum_out_total * inv_total;
    const float mean_sq = sumsq_out_total * inv_total;

    metrics.residual_energy = residual_energy_total;
    metrics.residual_persistence = persistence_total;
    metrics.pair_symmetry_drift = symmetry_total;
    metrics.diffusion_spread = diffusion_total;
    metrics.output_variance = mean_sq - mean_out * mean_out;

    return metrics;
}
#endif
