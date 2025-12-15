#include <cassert>
#include <cstddef>

#include "alm/core/phase3_operator.hpp"

int main() {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);
    Phase3Operator op(stencil);

    const std::size_t span = stencil.slice_span();
    auto* now = stencil.now_slice();
    auto* recent = stencil.recent_slice();

    for (std::size_t i = 0; i < span; i += 2) {
        const float value = static_cast<float>(i % 64) - 16.0F;
        now[i] = value;
        now[i + 1] = -value;
        recent[i] = value * 0.5F;
        recent[i + 1] = -value * 0.5F;
    }

    const auto metrics = op.tick();

    auto* future = stencil.future_slice();
    for (std::size_t i = 0; i < span; i += 2) {
        const float pair_sum = future[i] + future[i + 1];
        assert(pair_sum == 0.0F);
    }

    assert(metrics.lane_pairs_processed ==
           TensorCluster::kCells * TensorCluster::kRegisters *
               (TensorCluster::kSimdLanes / 2));
    assert(metrics.pair_symmetry_drift == 0.0F);
    assert(metrics.residual_energy > 0.0F);
    assert(metrics.residual_persistence > 0.0F);
    assert(metrics.output_variance > 0.0F);

    return 0;
}
