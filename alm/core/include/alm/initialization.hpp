#pragma once

#include "alm/config.hpp"
#include "alm/stencil.hpp"

#include <cstdint>

namespace alm::core {

inline float SeedToUnitFloat(std::uint64_t seed) {
  constexpr double scale = 1.0 / static_cast<double>(UINT64_C(0x1'0000'0000));
  const auto folded = static_cast<std::uint32_t>(seed >> 16U);
  return static_cast<float>(folded * scale);
}

inline void ClearPadding(RegisterArray &reg_array) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      const auto linear = block * kLaneCount + lane;
      if (IsPaddingLane(linear)) {
        reg_array.blocks[block].lanes[lane] = 0.0F;
      }
    }
  }
}

inline void InitializeFrame(Frame &frame, const SeedConfig &config = DefaultSeedConfig()) {
  for (std::size_t y = 0; y < kGridHeight; ++y) {
    for (std::size_t x = 0; x < kGridWidth; ++x) {
      const auto linear = LinearIndex(x, y);
      const auto addr = AddressForCell(x, y);

      frame.r.block(addr.block).lanes[addr.lane] = SeedToUnitFloat(LaneSeed(config, Register::kR, linear));
      frame.g.block(addr.block).lanes[addr.lane] = SeedToUnitFloat(LaneSeed(config, Register::kG, linear));
      frame.b.block(addr.block).lanes[addr.lane] = SeedToUnitFloat(LaneSeed(config, Register::kB, linear));
      frame.i.block(addr.block).lanes[addr.lane] = SeedToUnitFloat(LaneSeed(config, Register::kI, linear));
    }
  }

  ClearPadding(frame.r);
  ClearPadding(frame.g);
  ClearPadding(frame.b);
  ClearPadding(frame.i);
}

}  // namespace alm::core
