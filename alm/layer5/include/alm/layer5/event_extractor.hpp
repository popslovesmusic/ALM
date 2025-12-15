#pragma once

#include <array>
#include <cstdint>

#include "alm/core/persistence_probe.hpp"

namespace alm::layer5 {

struct EventRecord {
    std::uint64_t id;
    std::uint64_t timestamp;
    float spatial_index;
    float intensity;
    std::array<float, 4> features;
};

class EventExtractor {
   public:
    explicit EventExtractor(float softness = 0.5F);

    EventRecord extract(std::uint64_t timestamp,
                        float spatial_index,
                        const PersistenceObservations& observables);

   private:
    std::uint64_t next_id_;
    float softness_;

    static float smooth_value(float value, float softness);
};

}  // namespace alm::layer5

