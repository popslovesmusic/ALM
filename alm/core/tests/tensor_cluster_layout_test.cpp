#include <cassert>
#include <cstddef>
#include <cstdint>
#include <type_traits>

#include "alm/core/tensor_cluster.hpp"

static_assert(TensorCluster::kTimeSlices == 4);
static_assert(TensorCluster::kCells == 100);
static_assert(TensorCluster::kRegisters == 4);
static_assert(TensorCluster::kSimdLanes == 32);
static_assert(TensorCluster::kTotalValues ==
              TensorCluster::kTimeSlices * TensorCluster::kCells *
                  TensorCluster::kRegisters * TensorCluster::kSimdLanes);
static_assert(sizeof(TensorCluster) ==
              TensorCluster::kTotalValues * sizeof(TensorCluster::Value));
static_assert(sizeof(TensorCluster) < 256 * 1024);
static_assert(alignof(TensorCluster) >= 128);
static_assert(std::is_trivially_copyable_v<TensorCluster>);

int main() {
    TensorCluster cluster{};

    const auto address = reinterpret_cast<std::uintptr_t>(&cluster);
    assert(address % alignof(TensorCluster) == 0);

    const auto* base = reinterpret_cast<const std::byte*>(cluster.data);
    const auto* end = reinterpret_cast<const std::byte*>(
        cluster.data + TensorCluster::kTotalValues);
    const std::ptrdiff_t span = end - base;
    assert(span == static_cast<std::ptrdiff_t>(sizeof(cluster.data)));

    return 0;
}
