#include <string>

using std::string;

int Evaluate(const string& expression) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"expression"};
  GenericTestMain(args, "evaluate_rpn.tsv", &Evaluate, DefaultComparator{},
                  param_names);
  return 0;
}
