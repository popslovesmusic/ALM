cmake_minimum_required(VERSION 3.20)

<<<<<<< ours
=======
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

>>>>>>> theirs
add_library(alm_core INTERFACE)

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
  $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -mavx2 -fno-fast-math -ffp-contract=off>)

add_library(alm_core_checks OBJECT checks.cpp)
target_link_libraries(alm_core_checks PRIVATE alm_core)
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
