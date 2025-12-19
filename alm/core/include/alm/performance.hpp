#pragma once

#include "alm/constants.hpp"

#include <cstddef>

namespace alm::core {

// Count of stencil slices participating in the four-phase rotation.
inline constexpr std::size_t kStencilSlices = 4;

// Cache budget for the four-slice stencil payload (256 KiB envelope).
inline constexpr std::size_t kL2CacheBudgetBytes = 262144U;

// Derived payload sizing for residency enforcement.
inline constexpr std::size_t kSliceElements = kRegisterCount * kLaneBlocks * kLaneCount;
inline constexpr std::size_t kSliceBytes = kSliceElements * sizeof(float);
inline constexpr std::size_t kStencilBytes = kSliceBytes * kStencilSlices;

// Literal stencil payload size used for cross-language validation.
<<<<<<< ours
=======
inline constexpr std::size_t kSliceElementsLiteral = 512U;
inline constexpr std::size_t kSliceBytesLiteral = 2048U;
>>>>>>> theirs
inline constexpr std::size_t kStencilBytesLiteral = 8192U;

inline constexpr std::size_t kCacheHeadroomBytes = 253952U;

<<<<<<< ours
=======
static_assert(kSliceElements == kSliceElementsLiteral,
              "Slice element count must remain stable for residency proofing.");
static_assert(kSliceBytes == kSliceBytesLiteral,
              "Slice payload size must remain stable for residency proofing.");
>>>>>>> theirs
static_assert(kStencilBytes == kStencilBytesLiteral,
              "Stencil payload size must remain stable for residency proofing.");
static_assert(kStencilBytesLiteral <= kL2CacheBudgetBytes,
              "Stencil payload must remain within the L2 cache budget.");
static_assert(kCacheHeadroomBytes == (kL2CacheBudgetBytes - kStencilBytesLiteral),
              "Cache headroom literal must track computed budget margin.");
static_assert(kCacheHeadroomBytes > 0, "Stencil payload must leave positive L2 headroom.");

}  // namespace alm::core
