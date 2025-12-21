#include "alm/compliance.hpp"
#include "alm/initialization.hpp"
#include "alm/kernel.hpp"

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

  return CheckFrameEquivalence(snapshot, stencil.recent(), "rotation_geometry");
}

InvariantReport VerifyTopologyConsistency(const NeighborMap &topology = kCanonicalTopology) {
  InvariantReport report{};

  for (std::size_t linear = 0; linear < kCellCount; ++linear) {
    const auto [block, lane] = BlockAndLane(linear);
    const auto &neighbors = topology.for_cell(linear);

    if (neighbors.empty()) {
      report.passed = false;
      report.failures.push_back({"topology", "no_neighbors", Register::kR, block, lane, 0.0F, 0.0F});
    }
  }

  return report;
}

}  // namespace alm::core
