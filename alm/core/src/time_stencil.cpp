#include "alm/core/time_stencil.hpp"

TimeStencil::TimeStencil(TensorCluster& cluster)
    : cluster_(&cluster),
      i_stable_(0),
      i_recent_(1),
      i_now_(2),
      i_future_(3),
      rotation_count_(0),
      rotation_epoch_(0),
      future_write_count_(0),
      future_write_offset_(0),
      future_had_overwrite_(false) {}

void TimeStencil::ingest_write_future(Value value, std::size_t count) {
    const std::size_t span = slice_span();

    Value* future = future_slice();

    for (std::size_t i = 0; i < count; ++i) {
        const std::size_t offset =
            future_write_offset_.fetch_add(1, std::memory_order_relaxed);
        const std::size_t write_index = offset % span;

        if (offset >= span) {
            future_had_overwrite_.store(true, std::memory_order_relaxed);
        }

        future[write_index] = value;
    }

    future_write_count_.fetch_add(count, std::memory_order_relaxed);
}

TimeStencil::PressureSnapshot TimeStencil::tick_compute() {
    const std::size_t tick_id =
        rotation_count_.fetch_add(1, std::memory_order_relaxed);
    const std::size_t captured_epoch =
        rotation_epoch_.load(std::memory_order_relaxed);
    const std::size_t captured_writes =
        future_write_count_.exchange(0, std::memory_order_relaxed);
    const bool captured_overwrite =
        future_had_overwrite_.exchange(false, std::memory_order_relaxed);

    rotate_once();

    rotation_epoch_.fetch_add(1, std::memory_order_relaxed);
    future_write_offset_.store(0, std::memory_order_relaxed);

    return PressureSnapshot{.rotation_index = tick_id,
                             .rotation_epoch = captured_epoch,
                             .writes_captured = captured_writes,
                             .had_overwrite = captured_overwrite};
}

void TimeStencil::rotate_once() {
    const std::size_t recycled_index = i_stable_;

    i_stable_ = i_recent_;
    i_recent_ = i_now_;
    i_now_ = i_future_;
    i_future_ = recycled_index;
}

TimeStencil::Value* TimeStencil::future_slice() {
    const std::size_t span = slice_span();
    return cluster_->data + i_future_ * span;
}

std::size_t TimeStencil::slice_span() const {
    return TensorCluster::kCells * TensorCluster::kRegisters *
           TensorCluster::kSimdLanes;
}

