#pragma once

#include <cstddef>

#include "alm/core/persistence_probe.hpp"
#include "alm/core/selection_pressure.hpp"
#include "alm/core/time_stencil.hpp"

struct Phase4Metrics {
    std::size_t lane_pairs_processed;
    float mean_residual_energy;
    float mean_pressure_multiplier;
    float bandwidth_scale;
    PersistenceObservations observables;
};

class Phase4Kernel {
   public:
    explicit Phase4Kernel(TimeStencil& stencil);

    Phase4Metrics tick();

   private:
    TimeStencil* stencil_;
    SelectionPressure pressure_;
    PersistenceProbe probe_;
};

