

unsigned long ReverseBits(unsigned long x) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  GenericTestMain(args, "reverse_bits.tsv", &ReverseBits, DefaultComparator{},
                  param_names);
  return 0;
}
