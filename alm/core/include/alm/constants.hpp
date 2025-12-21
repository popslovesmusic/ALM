#pragma once

#include <cstddef>
#include <cstdint>

namespace alm::core {

// Grid geometry for the canonical 10x10 domain.
inline constexpr std::size_t kGridWidth = 10;
inline constexpr std::size_t kGridHeight = 10;
inline constexpr std::size_t kCellCount = kGridWidth * kGridHeight;

// Lane geometry: four AVX2-aligned blocks of 32 lanes each.
inline constexpr std::size_t kLaneCount = 32;
inline constexpr std::size_t kLaneBlocks = 4;
inline constexpr std::size_t kLanesPerRegister = kLaneBlocks * kLaneCount;

// Register count per cell (R, G, B, I).
inline constexpr std::size_t kRegisterCount = 4;

// Time stencil slices: FUTURE, NOW, RECENT, STABLE.
inline constexpr std::size_t kStencilSlices = 4;

// Topology: each cell connects to 12 symmetric neighbors in the toroidal grid.
inline constexpr std::size_t kNeighborCount = 12;

// Deterministic seed defaults for reproducible initialization.
inline constexpr std::uint64_t kDefaultSeed = 0xA1B2C3D4u;

// Validation tolerances for coefficient symmetry and normalization.
inline constexpr float kCoefficientTolerance = 1e-5F;
inline constexpr float kBiasNormalizationTolerance = 1e-5F;

}  // namespace alm::core
