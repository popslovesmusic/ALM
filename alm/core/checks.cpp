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
#include <limits>

>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
=======
#include <limits>

#include "alm/build.hpp"
>>>>>>> theirs
#include "alm/performance.hpp"
#include "alm/types.hpp"

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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
#ifndef __AVX2__
#error "Canonical ALM build requires AVX2 targeting."
#endif

#ifdef __FAST_MATH__
#error "Fast-math transforms violate deterministic floating-point semantics."
#endif

static_assert(std::numeric_limits<float>::is_iec559,
              "IEEE-754 binary32 support is required for deterministic layout.");

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
