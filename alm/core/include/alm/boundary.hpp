#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>
#include <cmath>

namespace alm::core {

// Smooth resonance envelope applied near the edges of the toroidal domain.
struct BoundaryProfile {
  std::array<float, kLanesPerRegister> envelope{};
};

inline constexpr float kPi = 3.14159265358979323846F;

inline float EdgeBlend(std::size_t coordinate, std::size_t extent) {
  const float normalized = static_cast<float>(coordinate) / static_cast<float>(extent - 1U);
  const float centered = std::fabs(0.5F - normalized) * 2.0F;
  return 0.5F * (1.0F + std::cos(kPi * centered));
}

inline float ResonanceAt(std::size_t x, std::size_t y, float interior_gain, float edge_gain) {
  const float blend_x = EdgeBlend(x, kGridWidth);
  const float blend_y = EdgeBlend(y, kGridHeight);
  const float radial = 0.5F * (blend_x + blend_y);
  return edge_gain * (1.0F - radial) + interior_gain * radial;
}

inline void BuildBoundaryProfile(float interior_gain, float edge_gain, BoundaryProfile &profile) {
  for (std::size_t y = 0; y < kGridHeight; ++y) {
    for (std::size_t x = 0; x < kGridWidth; ++x) {
      const std::size_t linear = y * kGridWidth + x;
      profile.envelope[linear] = ResonanceAt(x, y, interior_gain, edge_gain);
    }
  }

  for (std::size_t linear = kCellCount; linear < kLanesPerRegister; ++linear) {
    profile.envelope[linear] = 0.0F;
  }
}

inline void ApplyBoundaryCondition(const BoundaryProfile &profile, Frame &frame) {
  for (std::size_t y = 0; y < kGridHeight; ++y) {
    for (std::size_t x = 0; x < kGridWidth; ++x) {
      const auto [block, lane] = BlockAndLane(y * kGridWidth + x);
      const float weight = profile.envelope[y * kGridWidth + x];

      frame.r.blocks[block].lanes[lane] *= weight;
      frame.g.blocks[block].lanes[lane] *= weight;
      frame.b.blocks[block].lanes[lane] *= weight;
      frame.i.blocks[block].lanes[lane] *= weight;
    }
  }
}

}  // namespace alm::core

