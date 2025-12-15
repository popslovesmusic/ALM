#pragma once

#include <cstddef>
#include <vector>

#include "alm/core/time_stencil.hpp"

struct Phase3Metrics {
    std::size_t lane_pairs_processed;
    float residual_energy;
    float residual_persistence;
    float pair_symmetry_drift;
    float output_variance;
    float diffusion_spread;
};

class Phase3Operator {
   public:
    explicit Phase3Operator(TimeStencil& stencil);

    Phase3Metrics tick();

    const std::vector<Phase3Metrics>& metrics_log() const { return metrics_log_; }

   private:
    Phase3Metrics tick_scalar(TimeStencil::Value* now,
                              const TimeStencil::Value* recent,
                              TimeStencil::Value* future);

#if defined(__AVX2__)
    Phase3Metrics tick_avx2(TimeStencil::Value* now,
                            const TimeStencil::Value* recent,
                            TimeStencil::Value* future);
#endif

    TimeStencil* stencil_;
    std::vector<Phase3Metrics> metrics_log_;
};
