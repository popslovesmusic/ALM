#pragma once

#include "alm/core/tensor_cluster.hpp"

struct SelectionPressureResult {
    float pressured_residual;
    float local_multiplier;
};

class SelectionPressure {
   public:
    SelectionPressure();

    float bandwidth_scale(float mean_residual_energy) const;

    SelectionPressureResult apply(float residual,
                                  float neighbor_residual,
                                  float bandwidth_scale) const;

   private:
    float base_decay_rate_;
    float crowding_gain_;
    float diffusion_gain_;
    float bandwidth_alpha_;
};

