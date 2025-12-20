#pragma once

#include "alm/constants.hpp"
#include "alm/kernel.hpp"
#include "alm/types.hpp"

#include <array>
#include <cmath>
#include <cstddef>
#include <cstdint>

namespace alm::core {

struct RegisterMoments {
  float mean{0.0F};
  float energy{0.0F};
  float max_abs{0.0F};
};

struct FrameMoments {
  std::array<RegisterMoments, kRegisterCount> registers{};
  float total_energy{0.0F};
};

struct SpiralObservables {
  float radial_energy{0.0F};
  float angular_alignment{0.0F};
  float duality_ratio{0.0F};
};

struct ObservationSample {
  std::uint64_t step{0};
  FrameMoments frame{};
  SpiralObservables spiral{};
};

inline float SafeRatio(float numerator, float denominator, float epsilon = 1e-6F) {
  return numerator / (denominator + epsilon);
}

inline RegisterMoments ComputeRegisterMoments(const RegisterArray &reg) {
  RegisterMoments moments{};
  float sum = 0.0F;
  float energy = 0.0F;
  float max_abs = 0.0F;
  std::size_t count = 0;

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      const std::size_t linear_index = block * kLaneCount + lane;
      if (IsPaddingLane(linear_index)) {
        continue;
      }
      const float value = reg.blocks[block].lanes[lane];
      sum += value;
      energy += value * value;
      const float abs_value = std::fabs(value);
      if (abs_value > max_abs) {
        max_abs = abs_value;
      }
      ++count;
    }
  }

  moments.mean = (count > 0) ? sum / static_cast<float>(count) : 0.0F;
  moments.energy = energy;
  moments.max_abs = max_abs;
  return moments;
}

inline FrameMoments ComputeFrameMoments(const Frame &frame) {
  FrameMoments moments{};
  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (std::size_t reg_index = 0; reg_index < kRegisters.size(); ++reg_index) {
    const Register reg = kRegisters[reg_index];
    const RegisterMoments reg_moments = ComputeRegisterMoments(frame.registers(reg));
    moments.total_energy += reg_moments.energy;
    moments.registers[reg_index] = reg_moments;
  }

  return moments;
}

inline SpiralObservables ComputeSpiralObservables(const Frame &now, const Frame &recent, const Frame &stable) {
  SpiralObservables observables{};
  Frame fast{};
  Frame slow{};
  FrameDifference(now, recent, fast);
  FrameDifference(now, stable, slow);

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (auto reg : kRegisters) {
    const auto &fast_reg = fast.registers(reg);
    const auto &slow_reg = slow.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        const std::size_t linear_index = block * kLaneCount + lane;
        if (IsPaddingLane(linear_index)) {
          continue;
        }
        const float fast_value = fast_reg.blocks[block].lanes[lane];
        const float slow_value = slow_reg.blocks[block].lanes[lane];
        observables.radial_energy += slow_value * slow_value + fast_value * fast_value;
        observables.angular_alignment += fast_value * slow_value;
      }
    }
  }

  observables.duality_ratio = SafeRatio(observables.angular_alignment, observables.radial_energy);
  return observables;
}

template <std::size_t Capacity>
class ObservationBuffer {
 public:
  [[nodiscard]] constexpr std::size_t capacity() const { return Capacity; }

  [[nodiscard]] std::size_t size() const { return size_; }

  void record(std::uint64_t step, const Frame &now, const Frame &recent, const Frame &stable) {
    const FrameMoments frame_moments = ComputeFrameMoments(now);
    const SpiralObservables spiral = ComputeSpiralObservables(now, recent, stable);

    samples_[write_index_] = ObservationSample{step, frame_moments, spiral};
    write_index_ = (write_index_ + 1U) % Capacity;
    if (size_ < Capacity) {
      ++size_;
    }
  }

  [[nodiscard]] const ObservationSample &latest() const {
    const std::size_t index = (write_index_ + Capacity - 1U) % Capacity;
    return samples_[index];
  }

  [[nodiscard]] const ObservationSample &at(std::size_t index) const {
    assert(index < size_);
    return samples_[index];
  }

 private:
  std::array<ObservationSample, Capacity> samples_{};
  std::size_t write_index_{0};
  std::size_t size_{0};
};

}  // namespace alm::core

