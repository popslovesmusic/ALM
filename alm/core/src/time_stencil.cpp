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
      future_had_overwrite_(false),
      last_compute_ns_(0),
      last_ingest_ns_(0) {}

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

    const auto now = std::chrono::steady_clock::now().time_since_epoch();
    const auto nanos =
        static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::nanoseconds>(now)
                                       .count());
    last_ingest_ns_.store(nanos, std::memory_order_relaxed);
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

    const auto now = std::chrono::steady_clock::now().time_since_epoch();
    const auto nanos_now =
        static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::nanoseconds>(now)
                                       .count());
    const std::uint64_t last_compute =
        last_compute_ns_.exchange(nanos_now, std::memory_order_relaxed);
    const std::uint64_t last_ingest =
        last_ingest_ns_.load(std::memory_order_relaxed);

    rotate_once();

    rotation_epoch_.fetch_add(1, std::memory_order_relaxed);
    future_write_offset_.store(0, std::memory_order_relaxed);

    return PressureSnapshot{.rotation_index = tick_id,
                             .rotation_epoch = captured_epoch,
                             .writes_captured = captured_writes,
                             .had_overwrite = captured_overwrite,
                             .compute_delta_ns =
                                 last_compute == 0 ? 0 : nanos_now - last_compute,
                             .ingest_delta_ns =
                                 last_ingest == 0 ? 0 : nanos_now - last_ingest};
}

void TimeStencil::rotate_once() {
    const std::size_t recycled_index =
        i_stable_.load(std::memory_order_relaxed);
    const std::size_t recent_index = i_recent_.load(std::memory_order_relaxed);
    const std::size_t now_index = i_now_.load(std::memory_order_relaxed);
    const std::size_t future_index = i_future_.load(std::memory_order_relaxed);

    i_stable_.store(recent_index, std::memory_order_release);
    i_recent_.store(now_index, std::memory_order_release);
    i_now_.store(future_index, std::memory_order_release);
    i_future_.store(recycled_index, std::memory_order_release);
}

TimeStencil::Value* TimeStencil::now_slice() {
    const std::size_t span = slice_span();
    const std::size_t now_index = i_now_.load(std::memory_order_acquire);
    return cluster_->data + now_index * span;
}

const TimeStencil::Value* TimeStencil::now_slice() const {
    const std::size_t span = slice_span();
    const std::size_t now_index = i_now_.load(std::memory_order_acquire);
    return cluster_->data + now_index * span;
}

TimeStencil::Value* TimeStencil::recent_slice() {
    const std::size_t span = slice_span();
    const std::size_t recent_index = i_recent_.load(std::memory_order_acquire);
    return cluster_->data + recent_index * span;
}

const TimeStencil::Value* TimeStencil::recent_slice() const {
    const std::size_t span = slice_span();
    const std::size_t recent_index = i_recent_.load(std::memory_order_acquire);
    return cluster_->data + recent_index * span;
}

TimeStencil::Value* TimeStencil::stable_slice() {
    const std::size_t span = slice_span();
    const std::size_t stable_index = i_stable_.load(std::memory_order_acquire);
    return cluster_->data + stable_index * span;
}

const TimeStencil::Value* TimeStencil::stable_slice() const {
    const std::size_t span = slice_span();
    const std::size_t stable_index = i_stable_.load(std::memory_order_acquire);
    return cluster_->data + stable_index * span;
}

TimeStencil::Value* TimeStencil::future_slice() {
    const std::size_t span = slice_span();
    const std::size_t future_index = i_future_.load(std::memory_order_acquire);
    return cluster_->data + future_index * span;
}

std::size_t TimeStencil::slice_span() const {
    return TensorCluster::kCells * TensorCluster::kRegisters *
           TensorCluster::kSimdLanes;
}

