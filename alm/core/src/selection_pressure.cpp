#include "alm/core/selection_pressure.hpp"

SelectionPressure::SelectionPressure()
    : base_decay_rate_(0.025F),
      crowding_gain_(0.65F),
      diffusion_gain_(0.0F),
      bandwidth_alpha_(0.1F) {}

float SelectionPressure::bandwidth_scale(float mean_residual_energy) const {
    const float scaled_energy = bandwidth_alpha_ * mean_residual_energy;
    return 1.0F / (1.0F + scaled_energy);
}

SelectionPressureResult SelectionPressure::apply(float residual,
                                                 float neighbor_residual,
                                                 float bandwidth_scale) const {
    const float neighbor_energy = neighbor_residual * neighbor_residual;
    const float blended = residual + diffusion_gain_ * (neighbor_residual - residual);
    const float decay = 1.0F / (1.0F + base_decay_rate_ + crowding_gain_ * neighbor_energy);
    const float local_multiplier = decay * bandwidth_scale;

    return SelectionPressureResult{.pressured_residual = blended * local_multiplier,
                                   .local_multiplier = local_multiplier};
}

