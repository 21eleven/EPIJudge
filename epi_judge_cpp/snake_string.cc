#include <string>

using std::string;

string SnakeString(const string& s) {
  // Implement this placeholder.
  return "";
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  GenericTestMain(args, "snake_string.tsv", &SnakeString, DefaultComparator{},
                  param_names);
  return 0;
}
