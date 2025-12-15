#pragma once

#include <cstddef>

#include "alm/core/time_stencil.hpp"

struct PersistenceObservations {
    float residual_energy_density;
    float persistence_recent;
    float persistence_stable;
    float drift_energy;
    float recurrence_coherence;
};

class PersistenceProbe {
   public:
    explicit PersistenceProbe(const TimeStencil& stencil);

    PersistenceObservations sample() const;

   private:
    const TimeStencil* stencil_;
};

