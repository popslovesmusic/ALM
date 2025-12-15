#include <cassert>
#include <cstddef>

#include "alm/core/phase3_operator.hpp"

int main() {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);
    Phase3Operator op(stencil);

    const std::size_t span = stencil.slice_span();

    const std::size_t heavy_writes = span * 2 + 9;
    stencil.ingest_write_future(1.0F, heavy_writes);
    const auto pressure = stencil.tick_compute();
    assert(pressure.had_overwrite);

    auto* now = stencil.now_slice();
    auto* recent = stencil.recent_slice();
    for (std::size_t i = 0; i < span; ++i) {
        now[i] = static_cast<float>((i % 17) - 8);
        recent[i] = now[i] * 0.25F;
    }

    const auto metrics = op.tick();
    auto* future = stencil.future_slice();

    std::size_t non_zero = 0;
    for (std::size_t i = 0; i < span; ++i) {
        if (future[i] != 0.0F) {
            ++non_zero;
        }
    }

    assert(non_zero >= TensorCluster::kSimdLanes);

    assert(metrics.residual_energy > 0.0F);
    assert(metrics.diffusion_spread > 0.0F);
    assert(!op.metrics_log().empty());

    return 0;
}
