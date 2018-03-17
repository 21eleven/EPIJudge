#include <memory>
#include <vector>

#include "bst_node.h"
#include "test_framework/generic_test.h"

using std::unique_ptr;
using std::vector;

vector<int> FindKLargestInBST(const unique_ptr<BstNode<int>>& tree, int k) {
  // Implement this placeholder.
  return {};
}

int main(int argc, char* argv[]) {
  // The timeout is set to 15 seconds for each test case.
  // If your program ends with TIMEOUT error, and you want to try longer time
  // limit, you can extend the limit by changing the following line.
  std::chrono::seconds timeout_seconds{15};

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree", "k"};
  return GenericTestMain(args, timeout_seconds, "k_largest_values_in_bst.tsv",
                         &FindKLargestInBST,
                         &UnorderedComparator<std::vector<int>>, param_names);
}
