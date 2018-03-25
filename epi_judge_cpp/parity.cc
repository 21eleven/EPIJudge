short Parity(unsigned long x) {
  // Implement this placeholder.
  short parity = 0;
  while ( x > 0 ) {
	  parity ^= 1;
	  x = x & x - 1;
	}
  return parity;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x"};
  generic_test_main(argc, argv, param_names, "parity.tsv", &Parity);
  return 0;
}
