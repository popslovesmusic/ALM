#pragma once

#include <filesystem>
#include <string>
#include <vector>

#include "alm/layer5/event_trace.hpp"

namespace alm::layer5 {

class LongTermMemory {
   public:
    explicit LongTermMemory(std::filesystem::path storage_root);

    std::filesystem::path store_trace(const std::vector<EventRecord>& trace,
                                      const std::string& label) const;

    [[nodiscard]] std::vector<EventRecord> retrieve(const std::string& label) const;

   private:
    std::filesystem::path storage_root_;
};

}  // namespace alm::layer5

