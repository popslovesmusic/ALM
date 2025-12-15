#include <algorithm>
#include <cassert>
#include <cmath>

#include "alm/core/phase4_kernel.hpp"

namespace {
std::size_t cell_base(std::size_t cell) {
    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;
    return cell * cell_span;
}

float pair_residual(const TimeStencil::Value* slice, std::size_t cell) {
    const std::size_t base = cell_base(cell);
    return slice[base] - slice[base + 1];
}
}

int main() {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);
    Phase4Kernel kernel(stencil);

    const std::size_t span = stencil.slice_span();
    std::fill(stencil.now_slice(), stencil.now_slice() + span, 0.0F);
    std::fill(stencil.recent_slice(), stencil.recent_slice() + span, 0.0F);
    std::fill(stencil.stable_slice(), stencil.stable_slice() + span, 0.0F);

    const std::size_t dominant_base = cell_base(0);
    stencil.now_slice()[dominant_base] = 1.2F;
    stencil.now_slice()[dominant_base + 1] = 0.0F;
    stencil.recent_slice()[dominant_base] = 1.2F;
    stencil.recent_slice()[dominant_base + 1] = 0.0F;
    stencil.stable_slice()[dominant_base] = 1.2F;
    stencil.stable_slice()[dominant_base + 1] = 0.0F;

    const std::size_t suppressed_cell = TensorCluster::kCells - 1;
    const std::size_t suppressed_base = cell_base(suppressed_cell);
    stencil.now_slice()[suppressed_base] = 0.45F;
    stencil.now_slice()[suppressed_base + 1] = 0.0F;
    stencil.recent_slice()[suppressed_base] = 0.45F;
    stencil.recent_slice()[suppressed_base + 1] = 0.0F;
    stencil.stable_slice()[suppressed_base] = 0.45F;
    stencil.stable_slice()[suppressed_base + 1] = 0.0F;

    for (int i = 0; i < 8; ++i) {
        kernel.tick();
        stencil.tick_compute();
    }

    const auto* evolved = stencil.now_slice();
    const float dominant_residual = std::fabs(pair_residual(evolved, 0));
    const float suppressed_residual = std::fabs(pair_residual(evolved, suppressed_cell));

    assert(std::isfinite(dominant_residual));
    assert(std::isfinite(suppressed_residual));
    assert(dominant_residual > suppressed_residual);
    assert(suppressed_residual < 0.3F);
    assert(dominant_residual > 0.3F);

    return 0;
}

