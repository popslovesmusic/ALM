#include "alm/core/persistence_probe.hpp"

PersistenceProbe::PersistenceProbe(const TimeStencil& stencil)
    : stencil_(&stencil) {}

PersistenceObservations PersistenceProbe::sample() const {
    const auto* now = stencil_->now_slice();
    const auto* recent = stencil_->recent_slice();
    const auto* stable = stencil_->stable_slice();
    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;
    const std::size_t pair_count = TensorCluster::kCells * TensorCluster::kRegisters *
                                   (TensorCluster::kSimdLanes / 2);

    float energy = 0.0F;
    float persistence_recent = 0.0F;
    float persistence_stable = 0.0F;
    float drift = 0.0F;
    float recurrence = 0.0F;

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t offset = base + reg * register_span;
            for (std::size_t pair = 0; pair < TensorCluster::kSimdLanes / 2; ++pair) {
                const std::size_t even_index = offset + pair * 2;
                const std::size_t odd_index = even_index + 1;

                const float residual_now = now[even_index] - now[odd_index];
                const float residual_recent = recent[even_index] - recent[odd_index];
                const float residual_stable = stable[even_index] - stable[odd_index];

                energy += residual_now * residual_now;
                persistence_recent += residual_now * residual_recent;
                persistence_stable += residual_now * residual_stable;

                const float drift_delta = residual_now - residual_stable;
                drift += drift_delta * drift_delta;

                recurrence += (residual_recent * residual_stable);
            }
        }
    }

    const float inv_pairs = pair_count == 0 ? 0.0F : 1.0F / static_cast<float>(pair_count);

    PersistenceObservations observables{};
    observables.residual_energy_density = energy * inv_pairs;
    observables.persistence_recent = persistence_recent * inv_pairs;
    observables.persistence_stable = persistence_stable * inv_pairs;
    observables.drift_energy = drift * inv_pairs;
    observables.recurrence_coherence = recurrence * inv_pairs;

    return observables;
}

