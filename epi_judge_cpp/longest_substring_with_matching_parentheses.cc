#include <string>
#include <vector>

using std::string;
using std::vector;

int LongestMatchingParentheses(const string& s) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  GenericTestMain(args, "longest_substring_with_matching_parentheses.tsv",
                  &LongestMatchingParentheses, DefaultComparator{},
                  param_names);
  return 0;
}
