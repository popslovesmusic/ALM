#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>

namespace alm::core {

struct FocusState {
  Frame focus{};
  Frame drift{};
};

inline constexpr float kOrthogonalityEpsilon = 1e-6F;

inline float BlendScalar(float a, float b, float t) {
  return (1.0F - t) * a + t * b;
}

inline void BlendFrame(const Frame &source, float mix, Frame &destination) {
  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};
  for (auto reg : kRegisters) {
    auto &dest_reg = destination.registers(reg);
    const auto &source_reg = source.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        dest_reg.blocks[block].lanes[lane] = BlendScalar(dest_reg.blocks[block].lanes[lane],
                                                        source_reg.blocks[block].lanes[lane], mix);
      }
    }
  }
}

inline void UpdateFocusState(const Frame &candidate, const Frame &jitter, float jitter_gain, float persistence,
                             FocusState &state) {
  BlendFrame(candidate, 0.5F * jitter_gain, state.focus);
  BlendFrame(jitter, jitter_gain, state.drift);
  BlendFrame(state.drift, persistence, state.focus);
}

inline void ProjectFocusOrthogonalToPressure(const Frame &pressure, FocusState &state) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      const float pressure_r = pressure.r.blocks[block].lanes[lane];
      const float pressure_g = pressure.g.blocks[block].lanes[lane];
      const float pressure_b = pressure.b.blocks[block].lanes[lane];
      const float pressure_i = pressure.i.blocks[block].lanes[lane];

      const float focus_r = state.focus.r.blocks[block].lanes[lane];
      const float focus_g = state.focus.g.blocks[block].lanes[lane];
      const float focus_b = state.focus.b.blocks[block].lanes[lane];
      const float focus_i = state.focus.i.blocks[block].lanes[lane];

      const float dot = focus_r * pressure_r + focus_g * pressure_g + focus_b * pressure_b + focus_i * pressure_i;
      const float norm = pressure_r * pressure_r + pressure_g * pressure_g + pressure_b * pressure_b +
                         pressure_i * pressure_i + kOrthogonalityEpsilon;
      const float projection = dot / norm;

      state.focus.r.blocks[block].lanes[lane] = focus_r - projection * pressure_r;
      state.focus.g.blocks[block].lanes[lane] = focus_g - projection * pressure_g;
      state.focus.b.blocks[block].lanes[lane] = focus_b - projection * pressure_b;
      state.focus.i.blocks[block].lanes[lane] = focus_i - projection * pressure_i;
    }
  }
}

inline void ApplyFocusOverlay(const FocusState &state, float gain, Frame &frame) {
  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};
  for (auto reg : kRegisters) {
    auto &target = frame.registers(reg);
    const auto &overlay = state.focus.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        target.blocks[block].lanes[lane] += gain * overlay.blocks[block].lanes[lane];
      }
    }
  }
}

}  // namespace alm::core

