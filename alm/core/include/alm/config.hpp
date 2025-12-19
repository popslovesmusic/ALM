#pragma once

#include "alm/constants.hpp"
#include "alm/types.hpp"

#include <array>
#include <cstdint>

namespace alm::core {

struct SeedConfig {
  std::uint64_t base_seed{kDefaultSeed};
  std::array<std::uint64_t, kRegisterCount> register_salts{
      0x9E3779B185EBCA87ULL, 0xC2B2AE3D27D4EB4FULL, 0x165667B19E3779F9ULL,
      0x85EBCA77C2B2AE63ULL};
};

[[nodiscard]] constexpr SeedConfig DefaultSeedConfig() { return SeedConfig{}; }

inline std::uint64_t MixSeed(std::uint64_t value) {
  value ^= value >> 33U;
  value *= 0xff51afd7ed558ccdULL;
  value ^= value >> 33U;
  value *= 0xc4ceb9fe1a85ec53ULL;
  value ^= value >> 33U;
  return value;
}

[[nodiscard]] inline std::uint64_t LaneSeed(const SeedConfig &config, Register reg,
                                            std::size_t linear_index) {
  const auto reg_index = static_cast<std::size_t>(reg);
  const auto salted = config.base_seed ^ config.register_salts[reg_index];
  return MixSeed(salted ^ static_cast<std::uint64_t>(linear_index));
}

}  // namespace alm::core
