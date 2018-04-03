
short CountBits(unsigned int x) {
  // Implement this placeholder.
  short count = 0;
  while ( x > 0 ) {
	count++;
	x &= x--;
  }
  return count;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x"};
  generic_test_main(argc, argv, param_names, "count_bits.tsv", &CountBits);
  return 0;
}
