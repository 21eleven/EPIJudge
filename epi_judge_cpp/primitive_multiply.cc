
unsigned long Multiply(unsigned long x, unsigned long y) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  GenericTestMain(args, "primitive_multiply.tsv", &Multiply,
                  DefaultComparator{}, param_names);
  return 0;
}
