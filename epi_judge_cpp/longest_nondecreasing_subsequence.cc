#include <vector>

using std::vector;

int LongestNondecreasingSubsequenceLength(const vector<int>& A) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  GenericTestMain(args, "longest_nondecreasing_subsequence.tsv",
                  &LongestNondecreasingSubsequenceLength, DefaultComparator{},
                  param_names);
  return 0;
}
