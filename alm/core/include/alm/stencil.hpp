#pragma once

#include "alm/types.hpp"

#include <algorithm>
#include <array>
#include <utility>

namespace alm::core {

enum class SliceRole : std::size_t {
  kFuture = 0,
  kNow = 1,
  kRecent = 2,
  kStable = 3,
};

class Stencil {
 public:
  Stencil() = default;

  [[nodiscard]] constexpr Frame &future() { return frames_[order_[static_cast<std::size_t>(SliceRole::kFuture)]]; }
  [[nodiscard]] constexpr Frame &now() { return frames_[order_[static_cast<std::size_t>(SliceRole::kNow)]]; }
  [[nodiscard]] constexpr Frame &recent() { return frames_[order_[static_cast<std::size_t>(SliceRole::kRecent)]]; }
  [[nodiscard]] constexpr Frame &stable() { return frames_[order_[static_cast<std::size_t>(SliceRole::kStable)]]; }

  [[nodiscard]] constexpr const Frame &future() const { return frames_[order_[static_cast<std::size_t>(SliceRole::kFuture)]]; }
  [[nodiscard]] constexpr const Frame &now() const { return frames_[order_[static_cast<std::size_t>(SliceRole::kNow)]]; }
  [[nodiscard]] constexpr const Frame &recent() const { return frames_[order_[static_cast<std::size_t>(SliceRole::kRecent)]]; }
  [[nodiscard]] constexpr const Frame &stable() const { return frames_[order_[static_cast<std::size_t>(SliceRole::kStable)]]; }

  // Rotate stencil roles without copying: FUTURE → NOW → RECENT → STABLE.
  constexpr void Rotate() { std::rotate(order_.begin(), order_.begin() + 1, order_.end()); }

 private:
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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
  std::array<Frame, 4> frames_{};
  std::array<std::size_t, 4> order_{0, 1, 2, 3};
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
  static_assert(kStencilSlices == 4, "Stencil rotation requires four slices.");

  std::array<Frame, kStencilSlices> frames_{};
  std::array<std::size_t, kStencilSlices> order_{0, 1, 2, 3};
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
};

}  // namespace alm::core
