#include "alm/layer5/long_term_memory.hpp"

#include <fstream>
#include <iomanip>
#include <limits>

namespace alm::layer5 {

LongTermMemory::LongTermMemory(std::filesystem::path storage_root)
    : storage_root_(std::move(storage_root)) {
    std::filesystem::create_directories(storage_root_);
}

std::filesystem::path LongTermMemory::store_trace(const std::vector<EventRecord>& trace,
                                                  const std::string& label) const {
    const auto target = storage_root_ / (label + ".trace");
    std::ofstream out(target, std::ios::trunc);

    out << std::setprecision(9);
    for (const auto& event : trace) {
        out << event.id << ',' << event.timestamp << ',' << event.spatial_index << ','
            << event.intensity;
        for (const auto feature : event.features) {
            out << ',' << feature;
        }
        out << '\n';
    }

    return target;
}

std::vector<EventRecord> LongTermMemory::retrieve(const std::string& label) const {
    const auto target = storage_root_ / (label + ".trace");
    std::ifstream in(target);

    std::vector<EventRecord> events;
    if (!in.good()) {
        return events;
    }

    while (in.good()) {
        EventRecord record{};
        char comma;
        if (!(in >> record.id)) {
            break;
        }
        in >> comma >> record.timestamp >> comma >> record.spatial_index >> comma >> record.intensity;

        for (auto& feature : record.features) {
            in >> comma >> feature;
        }

        // consume newline
        in.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        events.push_back(record);
    }

    return events;
}

}  // namespace alm::layer5

