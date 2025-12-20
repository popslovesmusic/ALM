#pragma once

#include "alm/coefficients.hpp"
#include "alm/types.hpp"

#include <array>
#include <cmath>
#include <string_view>
#include <vector>

namespace alm::core {

struct ComparisonTolerance {
  float absolute{1e-6F};
  float relative{1e-4F};
};

struct InvariantViolation {
  std::string_view invariant;
  std::string_view reason;
  Register reg{Register::kR};
  std::size_t block{kLaneBlocks};
  std::size_t lane{kLaneCount};
  float observed{0.0F};
  float expected{0.0F};
};

struct InvariantReport {
  bool passed{true};
  std::vector<InvariantViolation> failures{};
};

inline bool ApproximatelyEqual(float lhs, float rhs, const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  const float diff = std::fabs(lhs - rhs);
  if (diff <= tolerance.absolute) {
    return true;
  }

  const float scale = std::max(std::fabs(lhs), std::fabs(rhs));
  return diff <= tolerance.relative * scale;
}

inline void NoteViolation(std::vector<InvariantViolation> &failures, std::string_view invariant,
                          std::string_view reason, Register reg, std::size_t block, std::size_t lane,
                          float observed, float expected) {
  failures.push_back({invariant, reason, reg, block, lane, observed, expected});
}

inline InvariantReport CheckFrameEquivalence(const Frame &baseline, const Frame &candidate,
                                             std::string_view invariant,
                                             const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  InvariantReport report{};

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (const Register reg : kRegisters) {
    const auto &lhs = baseline.registers(reg);
    const auto &rhs = candidate.registers(reg);

    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        const float lhs_value = lhs.blocks[block].lanes[lane];
        const float rhs_value = rhs.blocks[block].lanes[lane];
        if (!ApproximatelyEqual(lhs_value, rhs_value, tolerance)) {
          report.passed = false;
          NoteViolation(report.failures, invariant, "frame mismatch", reg, block, lane, rhs_value, lhs_value);
        }
      }
    }
  }

  return report;
}

inline InvariantReport CheckLanePermutationInvariant(const Frame &baseline, const Frame &permuted_then_unpermuted,
                                                     const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  return CheckFrameEquivalence(baseline, permuted_then_unpermuted, "lane_permutation", tolerance);
}

inline InvariantReport CheckPairedLaneAntisymmetry(const Frame &frame,
                                                   const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  InvariantReport report{};

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (const Register reg : kRegisters) {
    const auto &reg_values = frame.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        const auto conjugate_lane = kConjugateLaneMap[lane];
        const float value = reg_values.blocks[block].lanes[lane];
        const float paired_value = reg_values.blocks[block].lanes[conjugate_lane];
        if (!ApproximatelyEqual(value, -paired_value, tolerance)) {
          report.passed = false;
          NoteViolation(report.failures, "antisymmetry", "pair mismatch", reg, block, lane, value, -paired_value);
        }
      }
    }
  }

  return report;
}

inline InvariantReport CheckNeutralDrift(const Frame &before, const Frame &after,
                                         const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  return CheckFrameEquivalence(before, after, "neutral_input_neutrality", tolerance);
}

inline InvariantReport CheckContinuity(const Frame &baseline_output, const Frame &perturbed_output, float epsilon,
                                       const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  InvariantReport report{};

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (const Register reg : kRegisters) {
    const auto &base_reg = baseline_output.registers(reg);
    const auto &pert_reg = perturbed_output.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        const float base_value = base_reg.blocks[block].lanes[lane];
        const float pert_value = pert_reg.blocks[block].lanes[lane];
        const float diff = std::fabs(base_value - pert_value);
        const float scaled_tolerance = tolerance.relative * std::max(std::fabs(base_value), std::fabs(pert_value)) +
                                       tolerance.absolute * epsilon;
        if (diff > scaled_tolerance) {
          report.passed = false;
          NoteViolation(report.failures, "continuity", "sensitivity breach", reg, block, lane, diff, scaled_tolerance);
        }
      }
    }
  }

  return report;
}

inline InvariantReport CheckIsolation(const Frame &baseline, const Frame &probe,
                                      const std::array<bool, kLaneCount> &isolated_lanes,
                                      std::string_view invariant = "isolation",
                                      const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  InvariantReport report{};

  constexpr std::array<Register, kRegisterCount> kRegisters = {Register::kR, Register::kG, Register::kB, Register::kI};

  for (const Register reg : kRegisters) {
    const auto &base_reg = baseline.registers(reg);
    const auto &probe_reg = probe.registers(reg);
    for (std::size_t block = 0; block < kLaneBlocks; ++block) {
      for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
        if (!isolated_lanes[lane]) {
          continue;
        }
        const float base_value = base_reg.blocks[block].lanes[lane];
        const float probe_value = probe_reg.blocks[block].lanes[lane];
        if (!ApproximatelyEqual(base_value, probe_value, tolerance)) {
          report.passed = false;
          NoteViolation(report.failures, invariant, "isolated lane drift", reg, block, lane, probe_value, base_value);
        }
      }
    }
  }

  return report;
}

inline InvariantReport CheckAuxIsolation(const Frame &baseline, const Frame &probe,
                                         const std::array<bool, kLaneCount> &aux_lanes,
                                         const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  return CheckIsolation(baseline, probe, aux_lanes, "auxiliary_isolation", tolerance);
}

inline InvariantReport CheckObservabilityIsolation(const Frame &baseline, const Frame &probe,
                                                   const std::array<bool, kLaneCount> &observable_lanes,
                                                   const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  return CheckIsolation(baseline, probe, observable_lanes, "observability_isolation", tolerance);
}

inline InvariantReport CheckScalarSimdEquivalence(const Frame &scalar_output, const Frame &simd_output,
                                                  const ComparisonTolerance &tolerance = ComparisonTolerance{}) {
  return CheckFrameEquivalence(scalar_output, simd_output, "scalar_avx2_equivalence", tolerance);
}

}  // namespace alm::core

