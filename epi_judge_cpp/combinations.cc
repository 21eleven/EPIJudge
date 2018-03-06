#include <vector>

using std::vector;

vector<vector<int>> Combinations(int n, int k) {
  // Implement this placeholder.
  return {};
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  // The timeout is set to 15 seconds for each test case.
  // If your program ends with TIMEOUT error, and you want to try longer time
  // limit, you can extend the limit by changing the following line.
  std::chrono::seconds timeout_seconds{15};

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"n", "k"};
  return GenericTestMain(
      args, timeout_seconds, "combinations.tsv", &Combinations,
      &UnorderedComparator<std::vector<std::vector<int>>>, param_names);
}
