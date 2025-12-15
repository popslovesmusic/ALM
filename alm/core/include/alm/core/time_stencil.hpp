#pragma once

#include <atomic>
#include <cstddef>

#include "alm/core/tensor_cluster.hpp"

struct TimeStencil {
    using Value = TensorCluster::Value;

    struct PressureSnapshot {
        std::size_t rotation_index;
        std::size_t rotation_epoch;
        std::size_t writes_captured;
        bool had_overwrite;
    };

    explicit TimeStencil(TensorCluster& cluster);

    void ingest_write_future(Value value, std::size_t count);

    PressureSnapshot tick_compute();

private:
    void rotate_once();

    Value* future_slice();

    std::size_t slice_span() const;

    TensorCluster* cluster_;
    std::size_t i_stable_;
    std::size_t i_recent_;
    std::size_t i_now_;
    std::size_t i_future_;

    std::atomic<std::size_t> rotation_count_;
    std::atomic<std::size_t> rotation_epoch_;
    std::atomic<std::size_t> future_write_count_;
    std::atomic<std::size_t> future_write_offset_;
    std::atomic<bool> future_had_overwrite_;
};

