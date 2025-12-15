#pragma once

#include <cstddef>
#include <type_traits>

struct alignas(128) TensorCluster {
    using Value = float;

    static constexpr std::size_t kTimeSlices = 4;
    static constexpr std::size_t kCells = 100;
    static constexpr std::size_t kRegisters = 4;
    static constexpr std::size_t kSimdLanes = 32;
    static constexpr std::size_t kTotalValues =
        kTimeSlices * kCells * kRegisters * kSimdLanes;

    alignas(128) Value data[kTotalValues];
};

static_assert(std::is_standard_layout_v<TensorCluster>);
static_assert(sizeof(TensorCluster) < 256 * 1024);
static_assert(alignof(TensorCluster) >= 128);
static_assert(sizeof(TensorCluster::data[0]) == sizeof(float));
static_assert(TensorCluster::kTotalValues ==
              TensorCluster::kTimeSlices * TensorCluster::kCells *
                  TensorCluster::kRegisters * TensorCluster::kSimdLanes);
