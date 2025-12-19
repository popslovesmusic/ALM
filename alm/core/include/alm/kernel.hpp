#pragma once

#include "alm/coefficients.hpp"
#include "alm/stencil.hpp"
#include "alm/topology.hpp"
#include "alm/types.hpp"

#include <array>
#include <cstddef>

namespace alm::core {

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
                             float decay = 0.0F) {
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
}

}  // namespace alm::core

