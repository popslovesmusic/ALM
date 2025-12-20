cmake_minimum_required(VERSION 3.20)
project(ALMCore LANGUAGES CXX)

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

>>>>>>> theirs
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

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
add_subdirectory(alm/core)
