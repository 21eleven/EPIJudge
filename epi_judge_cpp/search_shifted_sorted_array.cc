#include <vector>

using std::vector;

int SearchSmallest(const vector<int>& A) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  GenericTestMain(args, "search_shifted_sorted_array.tsv", &SearchSmallest,
                  DefaultComparator{}, param_names);
  return 0;
}
