#include <cassert>
#include <cstdint>

#include "alm/layer5/event_extractor.hpp"
#include "alm/layer5/event_trace.hpp"

using alm::layer5::EventExtractor;
using alm::layer5::EventRecord;
using alm::layer5::EventTrace;

int main() {
    EventExtractor extractor(0.4F);
    EventTrace trace(4);

    const PersistenceObservations observables{
        .residual_energy_density = 0.25F,
        .persistence_recent = 0.6F,
        .persistence_stable = 0.4F,
        .drift_energy = 0.1F,
        .recurrence_coherence = 0.5F,
    };

    for (std::uint64_t i = 0; i < 3; ++i) {
        trace.append(extractor.extract(100 + i, static_cast<float>(i) * 0.1F, observables));
    }

    // Deterministic replay ordering.
    const auto replayed = trace.replay();
    assert(replayed.size() == 3);
    for (std::size_t i = 1; i < replayed.size(); ++i) {
        assert(replayed[i - 1].timestamp < replayed[i].timestamp);
    }

    // Smooth response: small perturbations cause small intensity deltas.
    auto baseline = replayed.front();
    auto perturbed = extractor.extract(200, 0.0F, PersistenceObservations{
                                                       .residual_energy_density = 0.26F,
                                                       .persistence_recent = 0.6F,
                                                       .persistence_stable = 0.4F,
                                                       .drift_energy = 0.11F,
                                                       .recurrence_coherence = 0.5F,
                                                   });
    const float delta = perturbed.intensity - baseline.intensity;
    assert(delta > 0.0F);
    assert(delta < 0.05F);

    // Repeat extraction to verify determinism for identical inputs.
    EventExtractor extractor_b(0.4F);
    const auto reference = extractor_b.extract(100, 0.0F, observables);
    const auto repeated = extractor_b.extract(100, 0.0F, observables);
    assert(reference.intensity == repeated.intensity);
    assert(reference.features == repeated.features);

    return 0;
}

