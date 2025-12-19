#pragma once

#include "alm/constants.hpp"

#include <array>
#include <cassert>
#include <cstdint>
#include <utility>

namespace alm::core {

enum class Register : std::uint8_t {
  kR = 0,
  kG = 1,
  kB = 2,
  kI = 3,
};

struct CellCoordinate {
  std::size_t x{};
  std::size_t y{};
};

struct LaneAddress {
  std::size_t block{};
  std::size_t lane{};
};

// AVX2-aligned block of 32 lanes.
struct alignas(32) RegisterBlock {
  std::array<float, kLaneCount> lanes{};
};

// Four AVX2 lane blocks per register to cover the 10x10 grid (with padding).
struct RegisterArray {
  std::array<RegisterBlock, kLaneBlocks> blocks{};

  [[nodiscard]] constexpr RegisterBlock &block(std::size_t index) {
    assert(index < blocks.size());
    return blocks[index];
  }

  [[nodiscard]] constexpr const RegisterBlock &block(std::size_t index) const {
    assert(index < blocks.size());
    return blocks[index];
  }
};

struct Frame {
  RegisterArray r{};
  RegisterArray g{};
  RegisterArray b{};
  RegisterArray i{};

  [[nodiscard]] constexpr RegisterArray &registers(Register reg) {
    switch (reg) {
      case Register::kR:
        return r;
      case Register::kG:
        return g;
      case Register::kB:
        return b;
      case Register::kI:
        return i;
    }
    return r;  // Unreachable but satisfies compiler paths.
  }

  [[nodiscard]] constexpr const RegisterArray &registers(Register reg) const {
    switch (reg) {
      case Register::kR:
        return r;
      case Register::kG:
        return g;
      case Register::kB:
        return b;
      case Register::kI:
        return i;
    }
    return r;  // Unreachable but satisfies compiler paths.
  }
};

[[nodiscard]] constexpr bool InBounds(std::size_t x, std::size_t y) {
  return x < kGridWidth && y < kGridHeight;
}

[[nodiscard]] constexpr std::size_t LinearIndex(std::size_t x, std::size_t y) {
  assert(InBounds(x, y));
  return y * kGridWidth + x;
}

[[nodiscard]] constexpr std::pair<std::size_t, std::size_t> BlockAndLane(std::size_t linear_index) {
  assert(linear_index < kLanesPerRegister);
  return {linear_index / kLaneCount, linear_index % kLaneCount};
}

[[nodiscard]] constexpr LaneAddress AddressForCell(std::size_t x, std::size_t y) {
  const auto linear_index = LinearIndex(x, y);
  const auto [block, lane] = BlockAndLane(linear_index);
  return LaneAddress{block, lane};
}

[[nodiscard]] constexpr bool IsPaddingLane(std::size_t linear_index) {
  return linear_index >= kCellCount && linear_index < kLanesPerRegister;
}

}  // namespace alm::core
