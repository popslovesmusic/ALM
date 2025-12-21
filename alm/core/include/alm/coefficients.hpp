#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>
#include <cassert>
#include <cmath>
#include <string_view>

namespace alm::core {

inline constexpr std::array<std::size_t, kLaneCount> kConjugateLaneMap = [] {
  std::array<std::size_t, kLaneCount> map{};
  for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
    map[lane] = kLaneCount - 1U - lane;
  }
  return map;
}();

static_assert(kLaneCount % 2U == 0U, "Lane count must be even for conjugate pairing.");
static_assert(kConjugateLaneMap.front() == kLaneCount - 1U, "Lane 0 must pair with the final lane.");
static_assert(kConjugateLaneMap.back() == 0U, "Last lane must pair with lane 0.");
static_assert(kConjugateLaneMap[1] == kLaneCount - 2U, "Lane pairing must be symmetric across the payload.");

struct LaneCoefficients {
  std::array<float, kLaneCount> alpha{};
  std::array<float, kLaneCount> beta{};
  std::array<float, kLaneCount> gamma{};
};

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

  [[nodiscard]] constexpr const RegisterGammaCoefficients &gamma_for(std::size_t reg_index) const {
    assert(reg_index < gamma.size());
    return gamma[reg_index];
  }
};

struct CoefficientTables {
  std::array<RegisterCoefficientTables, kLaneBlocks> blocks{};

  [[nodiscard]] constexpr const RegisterCoefficientTables &block(std::size_t index) const {
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
  const float delta = std::fabs(norm - 1.0F);
  if (delta > kCoefficientTolerance) {
    return {false, channel, "normalization_violation", kLaneCount};
  }
  return {true, channel, {}, kLaneCount};
}

[[nodiscard]] inline CanonicalizationStatus ValidateLaneCoefficients(const LaneCoefficients &coeffs,
                                                                     std::string_view channel) {
  if (!FiniteCoefficients(coeffs.alpha) || !FiniteCoefficients(coeffs.beta) || !FiniteCoefficients(coeffs.gamma)) {
    return {false, channel, "non_finite", kLaneCount};
  }

  const auto symmetry = ValidateSymmetry(coeffs.alpha, channel);
  if (!symmetry.ok) {
    return symmetry;
  }

  const auto beta_symmetry = ValidateSymmetry(coeffs.beta, channel);
  if (!beta_symmetry.ok) {
    return beta_symmetry;
<<<<<<< ours
  }

  const auto gamma_symmetry = ValidateSymmetry(coeffs.gamma, channel);
  if (!gamma_symmetry.ok) {
    return gamma_symmetry;
  }

  const auto alpha_norm = ValidateNormalization(coeffs.alpha, channel);
  if (!alpha_norm.ok) {
    return alpha_norm;
  }

  return ValidateNormalization(coeffs.beta, channel);
}

[[nodiscard]] inline CanonicalizationStatus ValidateCoefficients(const CoefficientTables &coefficients) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t reg = 0; reg < kRegisterCount; ++reg) {
      const auto &alpha = coefficients.blocks[block].alpha_for(reg).lanes;
      const auto &beta = coefficients.blocks[block].beta_for(reg).lanes;
      LaneCoefficients lane_coeffs{alpha, beta, coefficients.blocks[block].gamma_for(reg).for_source(reg).lanes};
      const auto status = ValidateLaneCoefficients(lane_coeffs, "block_coefficients");
      if (!status.ok) {
        return status;
      }
    }
  }

  return {true, "coefficients", {}, kLaneCount};
}

inline CoefficientTables BuildUniformCoefficients(float alpha = 0.5F, float beta = 0.5F, float gamma = 0.0F) {
  CoefficientTables tables{};

  std::array<float, kLaneCount> alpha_vector{};
  std::array<float, kLaneCount> beta_vector{};
  std::array<float, kLaneCount> gamma_vector{};

  for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
    alpha_vector[lane] = alpha;
    beta_vector[lane] = beta;
    gamma_vector[lane] = gamma;
=======
  }

  const auto gamma_symmetry = ValidateSymmetry(coeffs.gamma, channel);
  if (!gamma_symmetry.ok) {
    return gamma_symmetry;
  }

  const auto alpha_norm = ValidateNormalization(coeffs.alpha, channel);
  if (!alpha_norm.ok) {
    return alpha_norm;
>>>>>>> theirs
  }

  return ValidateNormalization(coeffs.beta, channel);
}

[[nodiscard]] inline CanonicalizationStatus ValidateCoefficients(const CoefficientTables &coefficients) {
  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t reg = 0; reg < kRegisterCount; ++reg) {
<<<<<<< ours
      tables.blocks[block].alpha[reg].lanes = alpha_vector;
      tables.blocks[block].beta[reg].lanes = beta_vector;

      for (std::size_t source = 0; source < kRegisterCount; ++source) {
        tables.blocks[block].gamma[reg].sources[source].lanes = gamma_vector;
=======
      const auto &coeff_block = coefficients.blocks[block];
      const auto &alpha = coeff_block.alpha_for(reg).lanes;
      const auto &beta = coeff_block.beta_for(reg).lanes;

      LaneCoefficients lane_coeffs{alpha, beta, coeff_block.gamma_for(reg).for_source(reg).lanes};
      const auto status = ValidateLaneCoefficients(lane_coeffs, "block_coefficients");
      if (!status.ok) {
        return status;
      }

      for (std::size_t source = 0; source < kRegisterCount; ++source) {
        const auto &gamma = coeff_block.gamma_for(reg).for_source(source).lanes;
        if (!FiniteCoefficients(gamma)) {
          return {false, "gamma", "non_finite", kLaneCount};
        }

        const auto gamma_symmetry = ValidateSymmetry(gamma, "gamma");
        if (!gamma_symmetry.ok) {
          return gamma_symmetry;
        }
>>>>>>> theirs
      }
    }
  }

<<<<<<< ours
=======
  return {true, "coefficients", {}, kLaneCount};
}

inline CoefficientTables BuildUniformCoefficients(float alpha = 0.5F, float beta = 0.5F, float gamma = 0.0F) {
  CoefficientTables tables{};

  std::array<float, kLaneCount> alpha_vector{};
  std::array<float, kLaneCount> beta_vector{};
  std::array<float, kLaneCount> gamma_vector{};

  for (std::size_t lane = 0; lane < kLaneCount; ++lane) {
    alpha_vector[lane] = alpha;
    beta_vector[lane] = beta;
    gamma_vector[lane] = gamma;
  }

  for (std::size_t block = 0; block < kLaneBlocks; ++block) {
    for (std::size_t reg = 0; reg < kRegisterCount; ++reg) {
      tables.blocks[block].alpha[reg].lanes = alpha_vector;
      tables.blocks[block].beta[reg].lanes = beta_vector;

      for (std::size_t source = 0; source < kRegisterCount; ++source) {
        tables.blocks[block].gamma[reg].sources[source].lanes = gamma_vector;
      }
    }
  }

>>>>>>> theirs
  return tables;
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
