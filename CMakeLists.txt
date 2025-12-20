cmake_minimum_required(VERSION 3.20)
project(ALMCore LANGUAGES CXX)

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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
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
if (NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
  message(FATAL_ERROR "Canonical ALM build requires 64-bit pointers for deterministic AVX2 layout.")
endif()

if (DEFINED CMAKE_CXX_BYTE_ORDER)
  if (NOT CMAKE_CXX_BYTE_ORDER STREQUAL "LITTLE_ENDIAN")
    message(FATAL_ERROR "Canonical ALM build requires little-endian layout for deterministic AVX2 packing.")
  endif()
else()
  include(TestBigEndian)
  TEST_BIG_ENDIAN(ALM_IS_BIG_ENDIAN)
  if (ALM_IS_BIG_ENDIAN)
    message(FATAL_ERROR "Canonical ALM build requires little-endian layout for deterministic AVX2 packing.")
  endif()
endif()

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
if (NOT CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  message(FATAL_ERROR "Canonical ALM build currently requires GCC or Clang for deterministic AVX2 enforcement.")
endif()

include(CheckCXXCompilerFlag)

set(_ALM_REQUIRED_FLAGS "-mavx2" "-fno-fast-math" "-ffp-contract=off")
foreach(flag IN LISTS _ALM_REQUIRED_FLAGS)
  string(REPLACE "-" "_" flag_var ${flag})
  check_cxx_compiler_flag(${flag} ALM_HAS${flag_var})
  if (NOT ALM_HAS${flag_var})
    message(FATAL_ERROR "Compiler does not support required flag ${flag} for deterministic AVX2 builds.")
  endif()
endforeach()

set(ALM_FORBIDDEN_FLAGS "-ffast-math" "-Ofast" "-ffinite-math-only" "-funsafe-math-optimizations")
set(ALM_FLAG_SCOPES
    CMAKE_CXX_FLAGS
    CMAKE_CXX_FLAGS_RELEASE
    CMAKE_CXX_FLAGS_RELWITHDEBINFO
    CMAKE_CXX_FLAGS_MINSIZEREL
    CMAKE_CXX_FLAGS_DEBUG)

foreach(flag IN LISTS ALM_FORBIDDEN_FLAGS)
  string(REPLACE "-" "\\-" _flag_pattern ${flag})
  foreach(scope IN LISTS ALM_FLAG_SCOPES)
    if (${scope} MATCHES "(^|[ ;])${_flag_pattern}([ ;]|$)")
      message(FATAL_ERROR "Forbidden compiler flag detected in ${scope}: ${flag}")
    endif()
  endforeach()
endforeach()

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
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

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
add_compile_options(-Wall -Wextra -Wpedantic -mavx2 -fno-fast-math -ffp-contract=off)

>>>>>>> theirs
=======
set(ALM_CANONICAL_COMPILE_OPTIONS
    -Wall -Wextra -Wpedantic -mavx2 -fno-fast-math -ffp-contract=off)

add_compile_options(${ALM_CANONICAL_COMPILE_OPTIONS})

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
set(ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST
    -Wall -Wextra -Wpedantic -mavx2 -fno-fast-math -ffp-contract=off
    CACHE INTERNAL "Canonical compile option allowlist")

set(ALM_CANONICAL_COMPILE_OPTIONS ${ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST})
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
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs
=======
list(JOIN ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST " " ALM_CANONICAL_COMPILE_OPTIONS_STRING)
>>>>>>> theirs

foreach(option IN LISTS ALM_CANONICAL_COMPILE_OPTIONS)
  list(FIND ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST ${option} _allow_idx)
  if (_allow_idx EQUAL -1)
    message(FATAL_ERROR "Non-canonical compile option detected: ${option}")
  endif()
endforeach()

foreach(option IN LISTS ALM_CANONICAL_COMPILE_OPTION_ALLOWLIST)
  list(FIND ALM_CANONICAL_COMPILE_OPTIONS ${option} _canon_idx)
  if (_canon_idx EQUAL -1)
    message(FATAL_ERROR "Canonical compile option missing: ${option}")
  endif()
endforeach()

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
add_compile_options(${ALM_CANONICAL_COMPILE_OPTIONS})

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
set(CMAKE_CXX_FLAGS "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}")
set(CMAKE_CXX_FLAGS_RELEASE "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}")
set(CMAKE_CXX_FLAGS_MINSIZEREL "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}")
set(CMAKE_CXX_FLAGS_DEBUG "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}")

add_compile_options(${ALM_CANONICAL_COMPILE_OPTIONS})

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
add_subdirectory(alm/core)
