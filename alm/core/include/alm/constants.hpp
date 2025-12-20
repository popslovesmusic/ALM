#pragma once

#include <cstddef>
#include <cstdint>

namespace alm::core {

// Grid geometry constants for the canonical 10x10 domain.
inline constexpr std::size_t kGridWidth = 10;
inline constexpr std::size_t kGridHeight = 10;
inline constexpr std::size_t kCellCount = kGridWidth * kGridHeight;

// Lane structure: four AVX2 lane blocks with 32 lanes each.
inline constexpr std::size_t kLaneCount = 32;
inline constexpr std::size_t kLaneBlocks = 4;
inline constexpr std::size_t kLanesPerRegister = kLaneBlocks * kLaneCount;

// Register count per cell (R, G, B, I).
inline constexpr std::size_t kRegisterCount = 4;

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
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

>>>>>>> theirs
=======
// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

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
// Four-slice time stencil: FUTURE, NOW, RECENT, STABLE.
inline constexpr std::size_t kStencilSlices = 4;

// Topology constants: each cell connects to 12 symmetric neighbors.
inline constexpr std::size_t kNeighborCount = 12;

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
// Deterministic seed defaults for reproducible initialization.
inline constexpr std::uint64_t kDefaultSeed = 0xA1B2C3D4u;

}  // namespace alm::core
