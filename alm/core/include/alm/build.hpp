#pragma once

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
=======
#include <bit>
>>>>>>> theirs
#include <limits>

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
=======
static_assert(__cplusplus >= 202002L, "Canonical builds require C++20 or later.");

>>>>>>> theirs
=======
static_assert(__cplusplus >= 202002L, "Canonical builds require C++20 or later.");

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
static_assert(__cplusplus >= 202002L, "Canonical builds require C++20 or later.");

static_assert(sizeof(void*) == 8, "Canonical builds require 64-bit pointers for AVX2 layout stability.");

static_assert(std::endian::native == std::endian::little,
              "Canonical builds require little-endian layout for deterministic packing.");

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
static_assert(std::numeric_limits<float>::radix == 2,
              "Binary32 radix must remain power-of-two for deterministic SIMD layout.");
static_assert(std::numeric_limits<float>::digits == 24,
              "Binary32 mantissa bits must remain 24 for AVX2 packing stability.");
static_assert(std::numeric_limits<float>::max_exponent == 128,
              "Binary32 max exponent must remain 128 for saturation equivalence.");
static_assert(std::numeric_limits<float>::min_exponent == -125,
              "Binary32 min exponent must remain -125 for underflow parity.");
static_assert(std::numeric_limits<float>::digits10 == 6,
              "Binary32 decimal precision must remain 6 digits for invariant reporting.");

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
}  // namespace alm::core
