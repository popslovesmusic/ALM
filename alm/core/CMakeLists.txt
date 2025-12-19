cmake_minimum_required(VERSION 3.20)

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
