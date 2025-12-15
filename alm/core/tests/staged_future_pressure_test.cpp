#include <cassert>
#include <cstddef>
#include <thread>
#include <chrono>

#include "alm/core/time_stencil.hpp"

auto main() -> int {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);

    stencil.ingest_write_future(1.0F, 10);
    std::this_thread::sleep_for(std::chrono::milliseconds(1));
    auto snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 0);
    assert(snapshot.rotation_epoch == 0);
    assert(snapshot.writes_captured == 10);
    assert(snapshot.had_overwrite == false);
    assert(snapshot.compute_delta_ns == 0);
    assert(snapshot.ingest_delta_ns >= 1'000'000);

    const std::size_t heavy_count =
        TensorCluster::kCells * TensorCluster::kRegisters *
        TensorCluster::kSimdLanes + 5;
    stencil.ingest_write_future(2.0F, heavy_count);
    std::this_thread::sleep_for(std::chrono::milliseconds(2));
    snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 1);
    assert(snapshot.rotation_epoch == 1);
    assert(snapshot.writes_captured == heavy_count);
    assert(snapshot.had_overwrite == true);
    assert(snapshot.compute_delta_ns >= 1'000'000);
    assert(snapshot.ingest_delta_ns >= 2'000'000);

    stencil.ingest_write_future(3.0F, 4);
    std::this_thread::sleep_for(std::chrono::milliseconds(2));
    snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 2);
    assert(snapshot.rotation_epoch == 2);
    assert(snapshot.writes_captured == 4);
    assert(snapshot.had_overwrite == false);
    assert(snapshot.compute_delta_ns >= 1'000'000);
    assert(snapshot.ingest_delta_ns >= 2'000'000);

    return 0;
}

