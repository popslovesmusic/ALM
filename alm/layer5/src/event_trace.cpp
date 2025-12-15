#include "alm/layer5/event_trace.hpp"

#include <algorithm>

namespace alm::layer5 {

EventTrace::EventTrace(std::size_t capacity)
    : buffer_(capacity), head_(0), filled_(0) {}

void EventTrace::append(const EventRecord& record) {
    if (buffer_.empty()) {
        return;
    }

    buffer_[head_] = record;
    head_ = (head_ + 1) % buffer_.size();
    filled_ = std::min(buffer_.size(), filled_ + 1);
}

std::vector<EventRecord> EventTrace::replay() const {
    std::vector<EventRecord> ordered;
    ordered.reserve(filled_);

    const std::size_t start = filled_ == buffer_.size() ? head_ : 0;
    for (std::size_t i = 0; i < filled_; ++i) {
        const std::size_t index = (start + i) % buffer_.size();
        ordered.push_back(buffer_[index]);
    }

    return ordered;
}

std::vector<EventRecord> EventTrace::recent(std::size_t count) const {
    const std::size_t clamped = std::min(count, filled_);
    std::vector<EventRecord> window;
    window.reserve(clamped);

    for (std::size_t i = 0; i < clamped; ++i) {
        const std::size_t offset = (buffer_.size() + head_ - 1 - i) % buffer_.size();
        window.push_back(buffer_[offset]);
    }

    std::reverse(window.begin(), window.end());
    return window;
}

}  // namespace alm::layer5

