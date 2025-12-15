#include <atomic>
#include <cassert>
#include <chrono>
#include <thread>

#include "alm/core/time_stencil.hpp"

int main() {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);

    std::atomic<std::size_t> ingest_batches{0};

    std::thread ingest_thread([&]() {
        for (std::size_t i = 0; i < 200; ++i) {
            stencil.ingest_write_future(1.0F, 8);
            ingest_batches.fetch_add(1, std::memory_order_relaxed);
            std::this_thread::sleep_for(std::chrono::microseconds(500));
        }
    });

    std::size_t compute_ticks = 0;
    std::size_t last_epoch = 0;
    while (compute_ticks < 80) {
        auto snapshot = stencil.tick_compute();
        assert(snapshot.rotation_index == compute_ticks);
        assert(snapshot.rotation_epoch == last_epoch);
        last_epoch = snapshot.rotation_epoch + 1;
        ++compute_ticks;
        std::this_thread::sleep_for(std::chrono::microseconds(750));
    }

    ingest_thread.join();

    auto final_snapshot = stencil.tick_compute();
    assert(final_snapshot.rotation_epoch >= compute_ticks);
    assert(ingest_batches.load(std::memory_order_relaxed) >= 1);

    return 0;
}
