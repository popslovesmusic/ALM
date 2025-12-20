#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>
#include <cassert>
#include <cmath>
#include <cstddef>
#include <string_view>

namespace alm::core {

inline constexpr float kCoefficientTolerance = 1e-6F;
inline constexpr float kBiasNormalizationTolerance = 1e-6F;

// Lane pairing map to enforce q[\bar{\ell}] = q[\ell] symmetry.
inline constexpr std::array<std::size_t, kLaneCount> kConjugateLaneMap = [] {
  std::array<std::size_t, kLaneCount> pairs{};
  for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
    pairs[lane] = (kLaneCount - 1U) - lane;
  }
  return pairs;
}();

static_assert(kLaneCount % 2U == 0U, "Lane count must be even for conjugate pairing.");
static_assert(kConjugateLaneMap.front() == kLaneCount - 1U, "Lane 0 must pair with the final lane.");
static_assert(kConjugateLaneMap.back() == 0U, "Last lane must pair with lane 0.");
static_assert(kConjugateLaneMap[1] == kLaneCount - 2U, "Lane pairing must be symmetric across the payload.");

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
struct LaneCoefficients {
  std::array<float, kLaneCount> alpha{};
  std::array<float, kLaneCount> beta{};
  std::array<float, kLaneCount> gamma{};
};

struct CoefficientTables {
  std::array<LaneCoefficients, kLaneBlocks> blocks{};

  [[nodiscard]] constexpr const LaneCoefficients &block(std::size_t index) const {
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
struct RegisterLaneCoefficients {
  std::array<float, kLaneCount> lanes{};
};

struct RegisterGammaCoefficients {
  std::array<RegisterLaneCoefficients, kRegisterCount> sources{};

  [[nodiscard]] constexpr const RegisterLaneCoefficients &for_source(std::size_t index) const {
    assert(index < sources.size());
    return sources[index];
  }
};

struct RegisterCoefficientTables {
  std::array<RegisterLaneCoefficients, kRegisterCount> alpha{};
  std::array<RegisterLaneCoefficients, kRegisterCount> beta{};
  std::array<RegisterGammaCoefficients, kRegisterCount> gamma{};  // target, source

  [[nodiscard]] constexpr const RegisterLaneCoefficients &alpha_for(std::size_t reg_index) const {
    assert(reg_index < alpha.size());
    return alpha[reg_index];
  }

  [[nodiscard]] constexpr const RegisterLaneCoefficients &beta_for(std::size_t reg_index) const {
    assert(reg_index < beta.size());
    return beta[reg_index];
  }

  [[nodiscard]] constexpr const RegisterGammaCoefficients &gamma_for(std::size_t target_index) const {
    assert(target_index < gamma.size());
    return gamma[target_index];
  }
};

struct CoefficientTables {
  std::array<RegisterCoefficientTables, kLaneBlocks> blocks{};

  [[nodiscard]] constexpr const RegisterCoefficientTables &block(std::size_t index) const {
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    assert(index < blocks.size());
    return blocks[index];
  }
};

struct CanonicalizationStatus {
  bool ok{true};
  std::string_view channel{};
  std::string_view reason{};
  std::size_t lane{kLaneCount};
};

[[nodiscard]] inline float L2Norm(const std::array<float, kLaneCount> &values) {
  float sum = 0.0F;
  for (float v : values) {
    sum += v * v;
  }
  return std::sqrt(sum);
}

[[nodiscard]] inline bool FiniteCoefficients(const std::array<float, kLaneCount> &values) {
  for (float v : values) {
    if (!std::isfinite(v)) {
      return false;
    }
  }
  return true;
}

[[nodiscard]] inline CanonicalizationStatus ValidateSymmetry(const std::array<float, kLaneCount> &values,
                                                             std::string_view channel) {
  for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
    const auto conjugate = kConjugateLaneMap[lane];
    const float delta = std::fabs(values[lane] - values[conjugate]);
    if (delta > kCoefficientTolerance) {
      return {false, channel, "symmetry_violation", lane};
    }
  }
  return {true, channel, {}, kLaneCount};
}

[[nodiscard]] inline CanonicalizationStatus ValidateNormalization(const std::array<float, kLaneCount> &values,
                                                                  std::string_view channel) {
  const float norm = L2Norm(values);
  if (std::fabs(norm - 1.0F) > kCoefficientTolerance) {
    return {false, channel, "normalization", kLaneCount};
  }
  return {true, channel, {}, kLaneCount};
}

[[nodiscard]] inline CanonicalizationStatus ValidateCoefficients(const std::array<float, kLaneCount> &values,
                                                                std::string_view channel) {
  if (!FiniteCoefficients(values)) {
    return {false, channel, "non_finite", kLaneCount};
  }
  const auto symmetry = ValidateSymmetry(values, channel);
  if (!symmetry.ok) {
    return symmetry;
  }
  return ValidateNormalization(values, channel);
}

[[nodiscard]] inline CanonicalizationStatus CanonicalizeCoefficients(
    const std::array<float, kLaneCount> &alpha, const std::array<float, kLaneCount> &beta,
    const std::array<float, kLaneCount> &gamma, CoefficientTables &output) {
  const auto alpha_ok = ValidateCoefficients(alpha, "alpha");
  if (!alpha_ok.ok) {
    return alpha_ok;
  }
  const auto beta_ok = ValidateCoefficients(beta, "beta");
  if (!beta_ok.ok) {
    return beta_ok;
  }
  const auto gamma_ok = ValidateCoefficients(gamma, "gamma");
  if (!gamma_ok.ok) {
    return gamma_ok;
  }

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    output.blocks[block].alpha = alpha;
    output.blocks[block].beta = beta;
    output.blocks[block].gamma = gamma;
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    for (std::size_t reg = 0; reg < kRegisterCount; ++reg) {
      output.blocks[block].alpha[reg].lanes = alpha;
      output.blocks[block].beta[reg].lanes = beta;

      for (std::size_t source = 0; source < kRegisterCount; ++source) {
        output.blocks[block].gamma[reg].sources[source].lanes = gamma;
      }
    }
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
  }

  return {};
}

inline void DerivePhiBias(const Frame &now, const Frame &recent, const Frame &stable, Frame &bias_out,
                          float now_weight = 0.25F, float recent_weight = 0.25F, float stable_weight = 0.5F) {
  const float weight_sum = now_weight + recent_weight + stable_weight;
  assert(std::fabs(weight_sum - 1.0F) <= kBiasNormalizationTolerance);

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
      bias_out.r.blocks[block].lanes[lane] = now_weight * now.r.blocks[block].lanes[lane] +
                                            recent_weight * recent.r.blocks[block].lanes[lane] +
                                            stable_weight * stable.r.blocks[block].lanes[lane];

      bias_out.g.blocks[block].lanes[lane] = now_weight * now.g.blocks[block].lanes[lane] +
                                            recent_weight * recent.g.blocks[block].lanes[lane] +
                                            stable_weight * stable.g.blocks[block].lanes[lane];

      bias_out.b.blocks[block].lanes[lane] = now_weight * now.b.blocks[block].lanes[lane] +
                                            recent_weight * recent.b.blocks[block].lanes[lane] +
                                            stable_weight * stable.b.blocks[block].lanes[lane];

      bias_out.i.blocks[block].lanes[lane] = now_weight * now.i.blocks[block].lanes[lane] +
                                            recent_weight * recent.i.blocks[block].lanes[lane] +
                                            stable_weight * stable.i.blocks[block].lanes[lane];
    }
  }
}

}  // namespace alm::core

