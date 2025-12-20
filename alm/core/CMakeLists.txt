cmake_minimum_required(VERSION 3.20)

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
if (NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
  message(FATAL_ERROR "Canonical ALM build requires 64-bit pointers for deterministic AVX2 layout.")
endif()

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
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
add_library(alm_core INTERFACE)

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
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
add_library(alm_core INTERFACE)

set_target_properties(alm_core PROPERTIES
  CXX_STANDARD 20
  CXX_STANDARD_REQUIRED YES
  CXX_EXTENSIONS NO)

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
target_include_directories(alm_core
    INTERFACE
      $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
      $<INSTALL_INTERFACE:include>)

target_compile_features(alm_core INTERFACE cxx_std_20)

target_compile_options(alm_core INTERFACE
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic>)
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)
>>>>>>> theirs
=======
=======
>>>>>>> theirs
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2>)

add_library(alm_core_checks OBJECT checks.cpp)
target_link_libraries(alm_core_checks PRIVATE alm_core)
<<<<<<< ours
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
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2 -fno-fast-math -ffp-contract=off>)

add_library(alm_core_checks OBJECT checks.cpp)
target_link_libraries(alm_core_checks PRIVATE alm_core)
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
