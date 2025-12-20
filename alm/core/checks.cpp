#include "alm/performance.hpp"
#include "alm/types.hpp"

namespace alm::core {

static_assert(alignof(RegisterBlock) == 32, "Register blocks must remain 32-byte aligned.");
static_assert(sizeof(RegisterBlock) == kRegisterBlockBytesLiteral,
              "Register block size must match literal residency budget.");
static_assert(sizeof(RegisterArray) == kRegisterArrayBytesLiteral,
              "Register array size must match literal residency budget.");
static_assert(sizeof(Frame) == kFrameBytesLiteral, "Frame size must match literal residency budget.");
static_assert(sizeof(Frame) == kSliceBytesLiteral, "Frame size must match slice literal budget.");
static_assert(kStencilSlices * sizeof(Frame) == kStencilBytesLiteral,
              "Stencil footprint must match literal residency budget.");
static_assert(kStencilBytesLiteral <= kL2CacheBudgetBytes,
              "Stencil footprint must remain within the L2 budget envelope.");

}  // namespace alm::core
