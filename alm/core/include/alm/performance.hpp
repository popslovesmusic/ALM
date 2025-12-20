#pragma once

#include "alm/constants.hpp"
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
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs
=======
#include "alm/types.hpp"
>>>>>>> theirs

#include <cstddef>

namespace alm::core {

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
// Count of stencil slices participating in the four-phase rotation.
inline constexpr std::size_t kStencilSlices = 4;

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
// Cache budget for the four-slice stencil payload (256 KiB envelope).
inline constexpr std::size_t kL2CacheBudgetBytes = 262144U;

// Derived payload sizing for residency enforcement.
inline constexpr std::size_t kSliceElements = kRegisterCount * kLaneBlocks * kLaneCount;
inline constexpr std::size_t kSliceBytes = kSliceElements * sizeof(float);
inline constexpr std::size_t kStencilBytes = kSliceBytes * kStencilSlices;

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
// Literal stencil payload size used for cross-language validation.
<<<<<<< ours
=======
inline constexpr std::size_t kSliceElementsLiteral = 512U;
inline constexpr std::size_t kSliceBytesLiteral = 2048U;
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
inline constexpr std::size_t kRegisterBlockBytes = sizeof(RegisterBlock);
inline constexpr std::size_t kRegisterArrayBytes = sizeof(RegisterArray);
inline constexpr std::size_t kFrameBytes = sizeof(Frame);
inline constexpr std::size_t kStencilBytesFromLayout = kFrameBytes * kStencilSlices;

// Literal stencil payload size used for cross-language validation.
inline constexpr std::size_t kRegisterBlockBytesLiteral = 128U;
inline constexpr std::size_t kRegisterArrayBytesLiteral = 512U;
inline constexpr std::size_t kFrameBytesLiteral = 2048U;
inline constexpr std::size_t kSliceElementsLiteral = 512U;
inline constexpr std::size_t kSliceBytesLiteral = 2048U;
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
inline constexpr std::size_t kStencilBytesLiteral = 8192U;

inline constexpr std::size_t kCacheHeadroomBytes = 253952U;

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
static_assert(alignof(RegisterBlock) == 32, "Register blocks must remain 32-byte aligned.");
static_assert(kRegisterBlockBytes == kRegisterBlockBytesLiteral,
              "Register block byte size must remain stable for residency proofing.");
static_assert(kRegisterArrayBytes == kRegisterArrayBytesLiteral,
              "Register array byte size must remain stable for residency proofing.");
static_assert(kFrameBytes == kFrameBytesLiteral,
              "Frame byte size must remain stable for residency proofing.");
static_assert(kFrameBytes == kSliceBytes, "Frame byte size must match derived slice bytes.");
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
static_assert(kSliceElements == kSliceElementsLiteral,
              "Slice element count must remain stable for residency proofing.");
static_assert(kSliceBytes == kSliceBytesLiteral,
              "Slice payload size must remain stable for residency proofing.");
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
static_assert(kStencilBytes == kStencilBytesLiteral,
              "Stencil payload size must remain stable for residency proofing.");
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
static_assert(kFrameBytesLiteral == kSliceBytesLiteral,
              "Frame literal byte size must match slice literal byte size.");
static_assert(kStencilBytes == kStencilBytesLiteral,
              "Stencil payload size must remain stable for residency proofing.");
static_assert(kStencilBytesFromLayout == kStencilBytes,
              "Stencil payload must be consistent across layout and geometry derivations.");
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
static_assert(kStencilBytesLiteral <= kL2CacheBudgetBytes,
              "Stencil payload must remain within the L2 cache budget.");
static_assert(kCacheHeadroomBytes == (kL2CacheBudgetBytes - kStencilBytesLiteral),
              "Cache headroom literal must track computed budget margin.");
static_assert(kCacheHeadroomBytes > 0, "Stencil payload must leave positive L2 headroom.");

}  // namespace alm::core
