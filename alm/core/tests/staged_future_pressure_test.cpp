#include <cassert>
#include <cstddef>

#include "alm/core/time_stencil.hpp"

auto main() -> int {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);

    stencil.ingest_write_future(1.0F, 10);
    auto snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 0);
    assert(snapshot.rotation_epoch == 0);
    assert(snapshot.writes_captured == 10);
    assert(snapshot.had_overwrite == false);

    const std::size_t heavy_count =
        TensorCluster::kCells * TensorCluster::kRegisters *
        TensorCluster::kSimdLanes + 5;
    stencil.ingest_write_future(2.0F, heavy_count);
    snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 1);
    assert(snapshot.rotation_epoch == 1);
    assert(snapshot.writes_captured == heavy_count);
    assert(snapshot.had_overwrite == true);

    stencil.ingest_write_future(3.0F, 4);
    snapshot = stencil.tick_compute();
    assert(snapshot.rotation_index == 2);
    assert(snapshot.rotation_epoch == 2);
    assert(snapshot.writes_captured == 4);
    assert(snapshot.had_overwrite == false);

    return 0;
}

