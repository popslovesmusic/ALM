#pragma once

#include <limits>

namespace alm::core {

#ifndef __AVX2__
#error "Canonical ALM build requires AVX2 targeting."
#endif

#ifdef __FAST_MATH__
#error "Fast-math transforms violate deterministic floating-point semantics."
#endif

#ifdef __FINITE_MATH_ONLY__
static_assert(__FINITE_MATH_ONLY__ == 0, "Finite-only math mode truncates IEEE-754 behavior.");
#endif

static_assert(std::numeric_limits<float>::is_iec559,
              "IEEE-754 binary32 support is required for deterministic layout.");

static_assert(sizeof(float) == 4, "Binary32 width must remain 4 bytes.");

}  // namespace alm::core
