#pragma once

#include "alm/boundary.hpp"
#include "alm/coefficients.hpp"
#include "alm/focus.hpp"
#include "alm/stencil.hpp"
#include "alm/topology.hpp"

#include <array>

namespace alm::core {

inline void ScalarKernelStep(Stencil &stencil, const CoefficientTables &coefficients, const NeighborMap &topology,
                             float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                             const FocusState *focus = nullptr, float focus_gain = 1.0F) {
  Frame neighbor_accum{};
  AggregateNeighbors(stencil.now(), topology, neighbor_accum);

  Frame &future = stencil.future();
  const Frame &current = stencil.now();
  const Frame &recent = stencil.recent();

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      for (std::size_t reg_index = 0; reg_index < kRegisterCount; ++reg_index) {
        const Register reg = kRegisters[reg_index];
        const auto &coeff_block = coefficients.block(block);

        const float alpha = coeff_block.alpha_for(reg_index).lanes[lane];
        const float beta = coeff_block.beta_for(reg_index).lanes[lane];

        float gamma_mix = 0.0F;
        for (std::size_t source = 0; source < kRegisterCount; ++source) {
          const float gamma = coeff_block.gamma_for(reg_index).for_source(source).lanes[lane];
          const auto &source_reg = neighbor_accum.registers(kRegisters[source]);
          gamma_mix += gamma * source_reg.blocks[block].lanes[lane];
        }

        const auto &reg_now = current.registers(reg);
        const auto &reg_neighbors = neighbor_accum.registers(reg);

        float value = alpha * reg_now.blocks[block].lanes[lane] + beta * reg_neighbors.blocks[block].lanes[lane] + gamma_mix;
        value -= decay * recent.registers(reg).blocks[block].lanes[lane];

        future.registers(reg).blocks[block].lanes[lane] = value;
      }
    }
  }

  if (focus != nullptr) {
    ApplyFocusOverlay(*focus, focus_gain, future);
  }

  if (boundary != nullptr) {
    ApplyBoundaryCondition(*boundary, future);
  }
}

inline void AdvanceStencil(Stencil &stencil, const CoefficientTables &coefficients, const NeighborMap &topology,
                           float decay = 0.0F, const BoundaryProfile *boundary = nullptr,
                           const FocusState *focus = nullptr, float focus_gain = 1.0F) {
  ScalarKernelStep(stencil, coefficients, topology, decay, boundary, focus, focus_gain);
  stencil.Rotate();
}

inline void InitializeStencil(Stencil &stencil, const SeedConfig &config = DefaultSeedConfig()) {
  InitializeFrame(stencil.now(), config);
  InitializeFrame(stencil.recent(), config);
  InitializeFrame(stencil.stable(), config);
  InitializeFrame(stencil.future(), config);
}

}  // namespace alm::core
