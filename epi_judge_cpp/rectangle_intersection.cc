#include <tuple>

#include "test_framework/fmt_print.h"
#include "test_framework/test_utils_serialization_traits.h"

struct Rectangle {
  int x, y, width, height;
};

Rectangle IntersectRectangle(const Rectangle& R1, const Rectangle& R2) {
  // Implement this placeholder.
  return {0, 0, 0, 0};
}

bool operator==(const Rectangle& r1, const Rectangle& r2) {
  return std::tie(r1.x, r1.y, r1.width, r1.height) ==
         std::tie(r2.x, r2.y, r2.width, r2.height);
}

template <>
struct SerializationTraits<Rectangle>
    : UserSerTraits<Rectangle, int, int, int, int> {};

std::ostream& operator<<(std::ostream& out, const Rectangle& r) {
  return PrintTo(out, std::make_tuple(r.x, r.y, r.width, r.height));
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  // The timeout is set to 15 seconds for each test case.
  // If your program ends with TIMEOUT error, and you want to try longer time
  // limit, you can extend the limit by changing the following line.
  std::chrono::seconds timeout_seconds{15};

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"R1", "R2"};
  return GenericTestMain(args, timeout_seconds, "rectangle_intersection.tsv",
                         &IntersectRectangle, DefaultComparator{}, param_names);
}
