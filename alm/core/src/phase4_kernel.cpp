#include "alm/core/phase4_kernel.hpp"

Phase4Kernel::Phase4Kernel(TimeStencil& stencil)
    : stencil_(&stencil), pressure_(), probe_(stencil) {}

Phase4Metrics Phase4Kernel::tick() {
    auto* now = stencil_->now_slice();
    auto* future = stencil_->future_slice();

    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;
    const std::size_t pair_count =
        TensorCluster::kCells * TensorCluster::kRegisters * (TensorCluster::kSimdLanes / 2);

    float residual_energy = 0.0F;

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t offset = base + reg * register_span;
            for (std::size_t pair = 0; pair < TensorCluster::kSimdLanes / 2; ++pair) {
                const std::size_t even_index = offset + pair * 2;
                const std::size_t odd_index = even_index + 1;

                const float residual_now = now[even_index] - now[odd_index];
                residual_energy += residual_now * residual_now;
            }
        }
    }

    const float mean_residual_energy = residual_energy / static_cast<float>(pair_count);
    const float bandwidth = pressure_.bandwidth_scale(mean_residual_energy);

    float mean_multiplier = 0.0F;

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        const std::size_t neighbor_base = ((cell + 1) % TensorCluster::kCells) * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t offset = base + reg * register_span;
            const std::size_t neighbor_offset = neighbor_base + reg * register_span;

            for (std::size_t pair = 0; pair < TensorCluster::kSimdLanes / 2; ++pair) {
                const std::size_t even_index = offset + pair * 2;
                const std::size_t odd_index = even_index + 1;

                const float residual = now[even_index] - now[odd_index];
                const float neighbor_residual =
                    now[neighbor_offset + pair * 2] - now[neighbor_offset + pair * 2 + 1];

                const SelectionPressureResult pressured =
                    pressure_.apply(residual, neighbor_residual, bandwidth);
                const float delta = 0.5F * (pressured.pressured_residual - residual);

                const float even_out = now[even_index] + delta;
                const float odd_out = now[odd_index] - delta;

                future[even_index] = even_out;
                future[odd_index] = odd_out;

                mean_multiplier += pressured.local_multiplier;
            }
        }
    }

    const float inv_pairs = 1.0F / static_cast<float>(pair_count);

    Phase4Metrics metrics{};
    metrics.lane_pairs_processed = pair_count;
    metrics.mean_residual_energy = mean_residual_energy;
    metrics.mean_pressure_multiplier = mean_multiplier * inv_pairs;
    metrics.bandwidth_scale = bandwidth;
    metrics.observables = probe_.sample();

    return metrics;
}

