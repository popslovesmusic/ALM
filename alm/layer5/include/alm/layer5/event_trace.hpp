#pragma once

#include <cstddef>
#include <vector>

#include "alm/layer5/event_extractor.hpp"

namespace alm::layer5 {

class EventTrace {
   public:
    explicit EventTrace(std::size_t capacity);

    void append(const EventRecord& record);

    [[nodiscard]] std::vector<EventRecord> replay() const;

    [[nodiscard]] std::vector<EventRecord> recent(std::size_t count) const;

    [[nodiscard]] std::size_t size() const { return filled_; }
    [[nodiscard]] std::size_t capacity() const { return buffer_.size(); }

   private:
    std::vector<EventRecord> buffer_;
    std::size_t head_;
    std::size_t filled_;
};

}  // namespace alm::layer5

