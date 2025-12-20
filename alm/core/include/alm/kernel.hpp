#pragma once

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
#include "alm/coefficients.hpp"
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
=======
#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
>>>>>>> theirs
#include "alm/stencil.hpp"
#include "alm/topology.hpp"
#include "alm/types.hpp"

#include <array>
#include <cstddef>
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours

namespace alm::core {

=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
#include <immintrin.h>

namespace alm::core {

static_assert(kLaneCount % 8U == 0U, "Lane count must be divisible by AVX2 width.");

inline void Avx2RegisterDifference(const RegisterArray &lhs, const RegisterArray &rhs, RegisterArray &output) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; lane += 8) {
      const __m256 lhs_vec = _mm256_load_ps(lhs.blocks[block].lanes.data() + lane);
      const __m256 rhs_vec = _mm256_load_ps(rhs.blocks[block].lanes.data() + lane);
      const __m256 diff = _mm256_sub_ps(lhs_vec, rhs_vec);
      _mm256_store_ps(output.blocks[block].lanes.data() + lane, diff);
    }
  }
}

inline void Avx2FrameDifference(const Frame &lhs, const Frame &rhs, Frame &output) {
  Avx2RegisterDifference(lhs.r, rhs.r, output.r);
  Avx2RegisterDifference(lhs.g, rhs.g, output.g);
  Avx2RegisterDifference(lhs.b, rhs.b, output.b);
  Avx2RegisterDifference(lhs.i, rhs.i, output.i);
}

inline __m256 LoadRegisterBlock(const RegisterArray &input, std::size_t block, std::size_t lane_offset) {
  return _mm256_load_ps(input.blocks[block].lanes.data() + lane_offset);
}

inline void StoreRegisterBlock(RegisterArray &output, std::size_t block, std::size_t lane_offset, __m256 value) {
  _mm256_store_ps(output.blocks[block].lanes.data() + lane_offset, value);
}

inline __m256 AccumulateCoupling(const Frame &neighbor_sum, const RegisterGammaCoefficients &gamma, std::size_t block,
                                 std::size_t lane_offset) {
  __m256 acc = _mm256_setzero_ps();

  const __m256 r = LoadRegisterBlock(neighbor_sum.r, block, lane_offset);
  const __m256 g = LoadRegisterBlock(neighbor_sum.g, block, lane_offset);
  const __m256 b = LoadRegisterBlock(neighbor_sum.b, block, lane_offset);
  const __m256 i = LoadRegisterBlock(neighbor_sum.i, block, lane_offset);

  const __m256 gamma_r = _mm256_loadu_ps(gamma.for_source(0).lanes.data() + lane_offset);
  const __m256 gamma_g = _mm256_loadu_ps(gamma.for_source(1).lanes.data() + lane_offset);
  const __m256 gamma_b = _mm256_loadu_ps(gamma.for_source(2).lanes.data() + lane_offset);
  const __m256 gamma_i = _mm256_loadu_ps(gamma.for_source(3).lanes.data() + lane_offset);

  acc = _mm256_add_ps(acc, _mm256_mul_ps(r, gamma_r));
  acc = _mm256_add_ps(acc, _mm256_mul_ps(g, gamma_g));
  acc = _mm256_add_ps(acc, _mm256_mul_ps(b, gamma_b));
  acc = _mm256_add_ps(acc, _mm256_mul_ps(i, gamma_i));

  return acc;
}

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
inline void RegisterDifference(const RegisterArray &lhs, const RegisterArray &rhs, RegisterArray &output) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      output.blocks[block].lanes[lane] = lhs.blocks[block].lanes[lane] - rhs.blocks[block].lanes[lane];
    }
  }
}

inline void FrameDifference(const Frame &lhs, const Frame &rhs, Frame &output) {
  RegisterDifference(lhs.r, rhs.r, output.r);
  RegisterDifference(lhs.g, rhs.g, output.g);
  RegisterDifference(lhs.b, rhs.b, output.b);
  RegisterDifference(lhs.i, rhs.i, output.i);
}

inline void ScalarKernelStep(Stencil &stencil, const CoefficientTables &coefficients,
                             const NeighborMap &topology = kCanonicalTopology, float pressure = 1.0F,
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
                             float decay = 0.0F) {
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
=======
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
>>>>>>> theirs
  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  const Frame &now = stencil.now();
  const Frame &recent = stencil.recent();
  const Frame &stable = stencil.stable();

  Frame neighbor_sum{};
  AggregateNeighbors(now, topology, neighbor_sum);

  Frame bias{};
  DerivePhiBias(now, recent, stable, bias);

  Frame fast_residual{};
  Frame slow_residual{};
  FrameDifference(now, recent, fast_residual);
  FrameDifference(now, stable, slow_residual);

  Frame &future = stencil.future();

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      for (std::size_t target = 0; target < kRegisterCount; ++target) {
        const Register target_reg = kRegisters[target];

        float coupling = 0.0F;
        for (std::size_t source = 0; source < kRegisterCount; ++source) {
          coupling += neighbor_sum.registers(kRegisters[source]).blocks[block].lanes[lane] *
                      coefficients.blocks[block].gamma_for(target).for_source(source).lanes[lane];
        }

        const float fast = fast_residual.registers(target_reg).blocks[block].lanes[lane];
        const float slow = slow_residual.registers(target_reg).blocks[block].lanes[lane];
        const float alpha = coefficients.blocks[block].alpha_for(target).lanes[lane];
        const float beta = coefficients.blocks[block].beta_for(target).lanes[lane];
        const float bias_value = bias.registers(target_reg).blocks[block].lanes[lane];
        const float now_value = now.registers(target_reg).blocks[block].lanes[lane];

        const float update = alpha * fast + beta * slow + coupling;
        future.registers(target_reg).blocks[block].lanes[lane] = now_value + pressure * (update + bias_value) - decay * slow;
      }
    }
  }
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
}

<<<<<<< ours
=======
inline void Avx2KernelStep(Stencil &stencil, const CoefficientTables &coefficients,
                           const NeighborMap &topology = kCanonicalTopology, float pressure = 1.0F,
                           float decay = 0.0F) {
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

  if (boundary != nullptr) {
    ApplyBoundaryCondition(*boundary, future);
  }

  if (focus != nullptr) {
    ApplyFocusOverlay(*focus, focus_gain, future);
  }
}

inline void Avx2KernelStep(Stencil &stencil, const CoefficientTables &coefficients,
                           const NeighborMap &topology = kCanonicalTopology, float pressure = 1.0F,
                           float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                           const FocusState *focus = nullptr, float focus_gain = 1.0F) {
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
  const Frame &now = stencil.now();
  const Frame &recent = stencil.recent();
  const Frame &stable = stencil.stable();

  Frame neighbor_sum{};
  AggregateNeighbors(now, topology, neighbor_sum);

  Frame bias{};
  DerivePhiBias(now, recent, stable, bias);

  Frame fast_residual{};
  Frame slow_residual{};
  Avx2FrameDifference(now, recent, fast_residual);
  Avx2FrameDifference(now, stable, slow_residual);

  Frame &future = stencil.future();

  const __m256 pressure_vec = _mm256_set1_ps(pressure);
  const __m256 decay_vec = _mm256_set1_ps(decay);

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    const auto &coeff_block = coefficients.blocks[block];

    for (std::size_t lane = 0; lane < kLaneCount; lane += 8) {
      const __m256 now_r = LoadRegisterBlock(now.r, block, lane);
      const __m256 now_g = LoadRegisterBlock(now.g, block, lane);
      const __m256 now_b = LoadRegisterBlock(now.b, block, lane);
      const __m256 now_i = LoadRegisterBlock(now.i, block, lane);

      const __m256 fast_r = LoadRegisterBlock(fast_residual.r, block, lane);
      const __m256 fast_g = LoadRegisterBlock(fast_residual.g, block, lane);
      const __m256 fast_b = LoadRegisterBlock(fast_residual.b, block, lane);
      const __m256 fast_i = LoadRegisterBlock(fast_residual.i, block, lane);

      const __m256 slow_r = LoadRegisterBlock(slow_residual.r, block, lane);
      const __m256 slow_g = LoadRegisterBlock(slow_residual.g, block, lane);
      const __m256 slow_b = LoadRegisterBlock(slow_residual.b, block, lane);
      const __m256 slow_i = LoadRegisterBlock(slow_residual.i, block, lane);

      const __m256 bias_r = LoadRegisterBlock(bias.r, block, lane);
      const __m256 bias_g = LoadRegisterBlock(bias.g, block, lane);
      const __m256 bias_b = LoadRegisterBlock(bias.b, block, lane);
      const __m256 bias_i = LoadRegisterBlock(bias.i, block, lane);

      const __m256 alpha_r = _mm256_loadu_ps(coeff_block.alpha_for(0).lanes.data() + lane);
      const __m256 alpha_g = _mm256_loadu_ps(coeff_block.alpha_for(1).lanes.data() + lane);
      const __m256 alpha_b = _mm256_loadu_ps(coeff_block.alpha_for(2).lanes.data() + lane);
      const __m256 alpha_i = _mm256_loadu_ps(coeff_block.alpha_for(3).lanes.data() + lane);

      const __m256 beta_r = _mm256_loadu_ps(coeff_block.beta_for(0).lanes.data() + lane);
      const __m256 beta_g = _mm256_loadu_ps(coeff_block.beta_for(1).lanes.data() + lane);
      const __m256 beta_b = _mm256_loadu_ps(coeff_block.beta_for(2).lanes.data() + lane);
      const __m256 beta_i = _mm256_loadu_ps(coeff_block.beta_for(3).lanes.data() + lane);

      const __m256 coupling_r = AccumulateCoupling(neighbor_sum, coeff_block.gamma_for(0), block, lane);
      const __m256 coupling_g = AccumulateCoupling(neighbor_sum, coeff_block.gamma_for(1), block, lane);
      const __m256 coupling_b = AccumulateCoupling(neighbor_sum, coeff_block.gamma_for(2), block, lane);
      const __m256 coupling_i = AccumulateCoupling(neighbor_sum, coeff_block.gamma_for(3), block, lane);

      const __m256 update_r = _mm256_add_ps(_mm256_add_ps(_mm256_mul_ps(alpha_r, fast_r), _mm256_mul_ps(beta_r, slow_r)), coupling_r);
      const __m256 update_g = _mm256_add_ps(_mm256_add_ps(_mm256_mul_ps(alpha_g, fast_g), _mm256_mul_ps(beta_g, slow_g)), coupling_g);
      const __m256 update_b = _mm256_add_ps(_mm256_add_ps(_mm256_mul_ps(alpha_b, fast_b), _mm256_mul_ps(beta_b, slow_b)), coupling_b);
      const __m256 update_i = _mm256_add_ps(_mm256_add_ps(_mm256_mul_ps(alpha_i, fast_i), _mm256_mul_ps(beta_i, slow_i)), coupling_i);

      const __m256 update_bias_r = _mm256_add_ps(update_r, bias_r);
      const __m256 update_bias_g = _mm256_add_ps(update_g, bias_g);
      const __m256 update_bias_b = _mm256_add_ps(update_b, bias_b);
      const __m256 update_bias_i = _mm256_add_ps(update_i, bias_i);

      const __m256 future_r = _mm256_add_ps(now_r, _mm256_sub_ps(_mm256_mul_ps(pressure_vec, update_bias_r), _mm256_mul_ps(decay_vec, slow_r)));
      const __m256 future_g = _mm256_add_ps(now_g, _mm256_sub_ps(_mm256_mul_ps(pressure_vec, update_bias_g), _mm256_mul_ps(decay_vec, slow_g)));
      const __m256 future_b = _mm256_add_ps(now_b, _mm256_sub_ps(_mm256_mul_ps(pressure_vec, update_bias_b), _mm256_mul_ps(decay_vec, slow_b)));
      const __m256 future_i = _mm256_add_ps(now_i, _mm256_sub_ps(_mm256_mul_ps(pressure_vec, update_bias_i), _mm256_mul_ps(decay_vec, slow_i)));

      StoreRegisterBlock(future.r, block, lane, future_r);
      StoreRegisterBlock(future.g, block, lane, future_g);
      StoreRegisterBlock(future.b, block, lane, future_b);
      StoreRegisterBlock(future.i, block, lane, future_i);
    }
  }
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
}

>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

  if (boundary != nullptr) {
    ApplyBoundaryCondition(*boundary, future);
  }

  if (focus != nullptr) {
    ApplyFocusOverlay(*focus, focus_gain, future);
  }
}

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
}  // namespace alm::core

