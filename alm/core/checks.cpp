#include "alm/compliance.hpp"
#include "alm/initialization.hpp"
#include "alm/kernel.hpp"

<<<<<<< ours
namespace alm::core {

InvariantReport VerifyInitializationDeterminism(const SeedConfig &config) {
  Frame first{};
  Frame second{};

  InitializeFrame(first, config);
  InitializeFrame(second, config);

  return CheckFrameEquivalence(first, second, "deterministic_initialization");
}

InvariantReport VerifyStencilRotation() {
  Stencil stencil{};
  InitializeStencil(stencil);

  Frame snapshot = stencil.now();
  stencil.Rotate();
=======
#include <array>
>>>>>>> theirs

  return CheckFrameEquivalence(snapshot, stencil.recent(), "rotation_geometry");
}

<<<<<<< ours
=======
InvariantReport VerifyInitializationDeterminism(const SeedConfig &config) {
  Frame first{};
  Frame second{};

  InitializeFrame(first, config);
  InitializeFrame(second, config);

  return CheckFrameEquivalence(first, second, "deterministic_initialization");
}

InvariantReport VerifyStencilRotation() {
  Stencil stencil{};
  InitializeStencil(stencil);

  Frame snapshot = stencil.now();
  stencil.Rotate();

  return CheckFrameEquivalence(snapshot, stencil.recent(), "rotation_geometry");
}

>>>>>>> theirs
InvariantReport VerifyTopologyConsistency(const NeighborMap &topology = kCanonicalTopology) {
  InvariantReport report{};

  for (std::size_t linear = 0; linear < kCellCount; ++linear) {
<<<<<<< ours
    const auto [block, lane] = BlockAndLane(linear);
    const auto &neighbors = topology.for_cell(linear);

    if (neighbors.empty()) {
      report.passed = false;
      report.failures.push_back({"topology", "no_neighbors", Register::kR, block, lane, 0.0F, 0.0F});
    }
=======
    const auto &neighbors = topology.for_cell(linear);

    if (neighbors.size() != kNeighborCount) {
      const auto [block, lane] = BlockAndLane(linear);
      report.passed = false;
      report.failures.push_back(
          {"topology", "neighbor_count", Register::kR, block, lane, static_cast<float>(neighbors.size()),
           static_cast<float>(kNeighborCount)});
      continue;
    }

    std::array<bool, kCellCount> seen_neighbors{};

    for (const auto &neighbor : neighbors) {
      const std::size_t neighbor_linear = neighbor.block * kLaneCount + neighbor.lane;
      if (neighbor_linear >= kCellCount) {
        const auto [block, lane] = BlockAndLane(linear);
        report.passed = false;
        report.failures.push_back({"topology", "padding_neighbor", Register::kR, block, lane,
                                   static_cast<float>(neighbor_linear), static_cast<float>(kCellCount - 1U)});
        continue;
      }

      if (seen_neighbors[neighbor_linear]) {
        const auto [block, lane] = BlockAndLane(linear);
        report.passed = false;
        report.failures.push_back({"topology", "duplicate_neighbor", Register::kR, block, lane,
                                   static_cast<float>(neighbor_linear), static_cast<float>(neighbor_linear)});
        continue;
      }

      seen_neighbors[neighbor_linear] = true;
    }
  }

  const float expected_weight = 1.0F / static_cast<float>(kNeighborCount);
  if (!ApproximatelyEqual(topology.weight, expected_weight)) {
    report.passed = false;
    report.failures.push_back({"topology", "weight_mismatch", Register::kR, kLaneBlocks, kLaneCount, topology.weight,
                               expected_weight});
>>>>>>> theirs
  }

  return report;
}

}  // namespace alm::core
