#include "alm/layer5/event_extractor.hpp"

#include <algorithm>
#include <cmath>

namespace alm::layer5 {

namespace {
float softplus(float value) {
    // Smoothly map input to positive range without hard thresholds.
    return std::log1p(std::exp(value));
}

float logistic(float value, float softness) {
    const float scaled = value * softness;
    return 1.0F / (1.0F + std::exp(-scaled));
}
}  // namespace

EventExtractor::EventExtractor(float softness)
    : next_id_(0), softness_(std::max(softness, 0.05F)) {}

EventRecord EventExtractor::extract(std::uint64_t timestamp,
                                    float spatial_index,
                                    const PersistenceObservations& observables) {
    // Combine observables into a smooth intensity value without discrete gating.
    const float residual = smooth_value(observables.residual_energy_density, softness_);
    const float persistence =
        smooth_value(observables.persistence_recent + observables.persistence_stable, softness_);
    const float drift = smooth_value(observables.drift_energy, softness_);
    const float coherence = smooth_value(observables.recurrence_coherence, softness_);

    const float blended = 0.25F * residual + 0.3F * persistence + 0.2F * drift + 0.25F * coherence;
    const float intensity = logistic(blended, softness_);

    EventRecord record{};
    record.id = next_id_++;
    record.timestamp = timestamp;
    record.spatial_index = spatial_index;
    record.intensity = intensity;
    record.features = {residual, persistence, drift, coherence};

    return record;
}

float EventExtractor::smooth_value(float value, float softness) {
    // Keep the mapping continuous and bounded to avoid threshold-like jumps.
    const float softened = softplus(value);
    return std::tanh(softened * softness);
}

}  // namespace alm::layer5

