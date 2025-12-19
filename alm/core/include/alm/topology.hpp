#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>
#include <cstddef>
#include <utility>

namespace alm::core {

using NeighborOffset = std::pair<int, int>;

// Twelve symmetric offsets matching the toroidal topology contract.
inline constexpr std::array<NeighborOffset, kNeighborCount> kNeighborOffsets = {{
    NeighborOffset{-1, 0}, NeighborOffset{1, 0}, NeighborOffset{0, -1}, NeighborOffset{0, 1},
    NeighborOffset{-2, 0}, NeighborOffset{2, 0}, NeighborOffset{0, -2}, NeighborOffset{0, 2},
    NeighborOffset{-1, -1}, NeighborOffset{-1, 1}, NeighborOffset{1, -1}, NeighborOffset{1, 1},
}};

constexpr std::size_t WrapIndex(std::size_t index, int delta, std::size_t modulus) {
  const int shifted = static_cast<int>(index) + delta;
  const int mod = shifted % static_cast<int>(modulus);
  return static_cast<std::size_t>(mod < 0 ? mod + static_cast<int>(modulus) : mod);
}

inline constexpr CellCoordinate WrapCoordinate(std::size_t x, std::size_t y, NeighborOffset offset) {
  return {WrapIndex(x, offset.second, kGridWidth), WrapIndex(y, offset.first, kGridHeight)};
}

struct NeighborMap {
  std::array<std::array<LaneAddress, kNeighborCount>, kCellCount> neighbors{};
  float weight{1.0F / static_cast<float>(kNeighborCount)};

  [[nodiscard]] constexpr const std::array<LaneAddress, kNeighborCount> &for_cell(std::size_t linear_index) const {
    return neighbors[linear_index];
  }

  [[nodiscard]] constexpr const std::array<LaneAddress, kNeighborCount> &for_cell(std::size_t x, std::size_t y) const {
    return for_cell(LinearIndex(x, y));
  }
};

inline constexpr NeighborMap BuildCanonicalNeighborMap() {
  NeighborMap map{};

  for (std::size_t y = 0; y < kGridHeight; ++y) {
    for (std::size_t x = 0; x < kGridWidth; ++x) {
      const std::size_t linear = LinearIndex(x, y);
      for (std::size_t idx = 0; idx < kNeighborCount; ++idx) {
        const auto coord = WrapCoordinate(x, y, kNeighborOffsets[idx]);
        const auto addr = AddressForCell(coord.x, coord.y);
        map.neighbors[linear][idx] = addr;
      }
    }
  }

  return map;
}

inline constexpr NeighborMap kCanonicalTopology = BuildCanonicalNeighborMap();

inline void AggregateNeighbors(const RegisterArray &input, const NeighborMap &topology, RegisterArray &output) {
  output = RegisterArray{};  // Reset output, padding lanes remain zeroed.

  for (std::size_t linear = 0; linear < kCellCount; ++linear) {
    float sum = 0.0F;
    for (const auto &neighbor : topology.for_cell(linear)) {
      sum += input.blocks[neighbor.block].lanes[neighbor.lane];
    }

    const auto [block, lane] = BlockAndLane(linear);
    output.blocks[block].lanes[lane] = sum * topology.weight;
  }
}

inline void AggregateNeighbors(const Frame &input, const NeighborMap &topology, Frame &output) {
  AggregateNeighbors(input.r, topology, output.r);
  AggregateNeighbors(input.g, topology, output.g);
  AggregateNeighbors(input.b, topology, output.b);
  AggregateNeighbors(input.i, topology, output.i);
}

}  // namespace alm::core

