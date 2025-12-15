#pragma once

#include <array>
#include <cstdint>
#include <vector>

#include "alm/layer5/event_extractor.hpp"
#include "alm/layer5/event_trace.hpp"

namespace alm::phase6 {

struct StructuralPoint {
    std::uint64_t id;
    float intensity;
    std::array<float, 3> coordinates;
};

struct StructuralAtlas {
    std::vector<StructuralPoint> points;
};

class StructuralProjection {
   public:
    [[nodiscard]] StructuralAtlas project(const std::vector<alm::layer5::EventRecord>& events) const;

    [[nodiscard]] StructuralAtlas project(const alm::layer5::EventTrace& trace) const;
};

}  // namespace alm::phase6

