#include "alm/phase6/structural_projection.hpp"

namespace alm::phase6 {

StructuralAtlas StructuralProjection::project(
    const std::vector<alm::layer5::EventRecord>& events) const {
    StructuralAtlas atlas;
    atlas.points.reserve(events.size());

    for (const auto& event : events) {
        StructuralPoint point{};
        point.id = event.id;
        point.intensity = event.intensity;
        point.coordinates = {0.0F, 0.0F, 0.0F};
        atlas.points.push_back(point);
    }

    return atlas;
}

StructuralAtlas StructuralProjection::project(const alm::layer5::EventTrace& trace) const {
    const auto events = trace.replay();
    return project(events);
}

}  // namespace alm::phase6

