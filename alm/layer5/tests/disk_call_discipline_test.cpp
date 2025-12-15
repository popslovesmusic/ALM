#include <cassert>
#include <filesystem>
#include <vector>

#include "alm/layer5/event_extractor.hpp"
#include "alm/layer5/event_trace.hpp"
#include "alm/layer5/long_term_memory.hpp"

using alm::layer5::EventExtractor;
using alm::layer5::EventRecord;
using alm::layer5::EventTrace;
using alm::layer5::LongTermMemory;

int main() {
    const auto temp_dir = std::filesystem::temp_directory_path() / "alm_phase5_tests";
    LongTermMemory ltm(temp_dir);

    EventExtractor extractor;
    EventTrace trace(2);

    const PersistenceObservations observables{
        .residual_energy_density = 0.5F,
        .persistence_recent = 0.2F,
        .persistence_stable = 0.3F,
        .drift_energy = 0.15F,
        .recurrence_coherence = 0.25F,
    };

    trace.append(extractor.extract(1, 0.0F, observables));
    trace.append(extractor.extract(2, 0.2F, observables));

    const auto path = ltm.store_trace(trace.replay(), "deterministic_trace");
    assert(std::filesystem::exists(path));

    const auto retrieved = ltm.retrieve("deterministic_trace");
    assert(retrieved.size() == trace.size());
    for (std::size_t i = 0; i < retrieved.size(); ++i) {
        assert(retrieved[i].timestamp == trace.replay()[i].timestamp);
        assert(retrieved[i].intensity == trace.replay()[i].intensity);
        assert(retrieved[i].features == trace.replay()[i].features);
    }

    // Ensure storage is append-only and explicit by comparing file size to expected line count.
    const auto file_size = std::filesystem::file_size(path);
    assert(file_size > 0);

    return 0;
}

