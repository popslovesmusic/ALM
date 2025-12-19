#pragma once

#include "alm/stencil.hpp"
#include "alm/types.hpp"

#include <cstdint>
#include <span>
#include <utility>

namespace alm::core {

struct IngestSignal {
  CellCoordinate coord{};
  float value{};
};

enum class IngestStatus {
  kOk = 0,
  kStepMismatch,
  kInvalidChannel,
  kOutOfBounds,
};

struct IngestContext {
  std::uint64_t expected_step{0};
  Register channel{Register::kI};

  [[nodiscard]] constexpr bool ValidChannel(Register reg) const { return reg == Register::kI && reg == channel; }
};

inline IngestStatus ApplyIngest(IngestContext &context, Stencil &stencil, std::span<const IngestSignal> signals,
                                std::uint64_t step, Register target_register = Register::kI) {
  if (step != context.expected_step) {
    return IngestStatus::kStepMismatch;
  }
  if (!context.ValidChannel(target_register)) {
    return IngestStatus::kInvalidChannel;
  }

  auto &target = stencil.future().registers(target_register);
  for (const auto &signal : signals) {
    if (!InBounds(signal.coord.x, signal.coord.y)) {
      return IngestStatus::kOutOfBounds;
    }

    const auto addr = AddressForCell(signal.coord.x, signal.coord.y);
    target.block(addr.block).lanes[addr.lane] += signal.value;
  }

  return IngestStatus::kOk;
}

inline void AdvanceIngest(IngestContext &context) { ++context.expected_step; }

}  // namespace alm::core

