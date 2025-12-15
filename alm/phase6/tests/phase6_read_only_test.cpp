#include <algorithm>
#include <array>
#include <cassert>
#include <numeric>
#include <vector>

#include "alm/layer5/event_extractor.hpp"
#include "alm/layer5/event_trace.hpp"
#include "alm/phase6/structural_projection.hpp"

using alm::layer5::EventExtractor;
using alm::layer5::EventRecord;
using alm::layer5::EventTrace;

int main() {
    EventExtractor extractor(0.5F);
    EventTrace trace(4);

    const PersistenceObservations observables{
        .residual_energy_density = 0.4F,
        .persistence_recent = 0.3F,
        .persistence_stable = 0.2F,
        .drift_energy = 0.1F,
        .recurrence_coherence = 0.35F,
    };

    trace.append(extractor.extract(10, 0.0F, observables));
    trace.append(extractor.extract(11, 0.1F, observables));
    trace.append(extractor.extract(12, 0.2F, observables));

    const auto baseline = trace.replay();
    const float baseline_intensity_sum =
        std::accumulate(baseline.begin(), baseline.end(), 0.0F, [](float sum, const EventRecord& record) {
            return sum + record.intensity;
        });

    alm::phase6::StructuralProjection projection;
    const auto atlas_from_trace = projection.project(trace);
    const auto atlas_from_events = projection.project(baseline);

    const auto after_invocation = trace.replay();
    assert(after_invocation.size() == baseline.size());
    for (std::size_t i = 0; i < after_invocation.size(); ++i) {
        assert(after_invocation[i].id == baseline[i].id);
        assert(after_invocation[i].timestamp == baseline[i].timestamp);
        assert(after_invocation[i].intensity == baseline[i].intensity);
        assert(after_invocation[i].features == baseline[i].features);
    }

    assert(atlas_from_trace.points.size() == baseline.size());
    for (std::size_t i = 0; i < atlas_from_trace.points.size(); ++i) {
        assert(atlas_from_trace.points[i].id == baseline[i].id);
        assert(atlas_from_trace.points[i].intensity == baseline[i].intensity);
        assert((atlas_from_trace.points[i].coordinates == std::array<float, 3>{0.0F, 0.0F, 0.0F}));
    }

    assert(atlas_from_events.points.size() == atlas_from_trace.points.size());
    for (std::size_t i = 0; i < atlas_from_events.points.size(); ++i) {
        assert(atlas_from_events.points[i].id == atlas_from_trace.points[i].id);
        assert(atlas_from_events.points[i].intensity == atlas_from_trace.points[i].intensity);
        assert(atlas_from_events.points[i].coordinates == atlas_from_trace.points[i].coordinates);
    }

    const float post_projection_sum = std::accumulate(after_invocation.begin(),
                                                      after_invocation.end(),
                                                      0.0F,
                                                      [](float sum, const EventRecord& record) {
                                                          return sum + record.intensity;
                                                      });
    assert(post_projection_sum == baseline_intensity_sum);

    return 0;
}

