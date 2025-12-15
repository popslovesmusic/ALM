#include <algorithm>
#include <cassert>
#include <cmath>

#include "alm/core/phase4_kernel.hpp"

namespace {
void fill_slice(TimeStencil::Value* slice, std::size_t span, float value) {
    std::fill(slice, slice + span, value);
}
}

int main() {
    TensorCluster cluster{};
    TimeStencil stencil(cluster);
    Phase4Kernel kernel(stencil);

    const std::size_t span = stencil.slice_span();

    fill_slice(stencil.now_slice(), span, 0.0F);
    fill_slice(stencil.recent_slice(), span, 0.0F);
    fill_slice(stencil.stable_slice(), span, 0.0F);

    kernel.tick();

    auto* future = stencil.future_slice();
    for (std::size_t i = 0; i < span; ++i) {
        assert(std::fabs(future[i]) < 1e-6F);
    }

    const std::size_t register_span = TensorCluster::kSimdLanes;
    const std::size_t cell_span = TensorCluster::kRegisters * register_span;

    for (std::size_t cell = 0; cell < TensorCluster::kCells; ++cell) {
        const std::size_t base = cell * cell_span;
        for (std::size_t reg = 0; reg < TensorCluster::kRegisters; ++reg) {
            const std::size_t offset = base + reg * register_span;
            for (std::size_t pair = 0; pair < TensorCluster::kSimdLanes / 2; ++pair) {
                const float flat_value = 0.25F + 0.05F * static_cast<float>(pair);
                const std::size_t even_index = offset + pair * 2;
                const std::size_t odd_index = even_index + 1;

                stencil.now_slice()[even_index] = flat_value;
                stencil.now_slice()[odd_index] = flat_value;
                stencil.recent_slice()[even_index] = flat_value;
                stencil.recent_slice()[odd_index] = flat_value;
                stencil.stable_slice()[even_index] = flat_value;
                stencil.stable_slice()[odd_index] = flat_value;
            }
        }
    }

    kernel.tick();

    future = stencil.future_slice();
    for (std::size_t i = 0; i < span; ++i) {
        assert(std::fabs(future[i] - stencil.now_slice()[i]) < 1e-6F);
    }

    return 0;
}

