int Divide(int x, int y) {
  // Implement this placeholder.
  int result = 0;
  short power = 32;
  while (x >= y) {
	while (1 << power > x) {
		power--;
	}
	x -= y << power;
	result += 1 << power;
  }
  return result;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x", "y"};
  generic_test_main(argc, argv, param_names, "primitive_divide.tsv", &Divide);
  return 0;
}
