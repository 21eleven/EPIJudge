#include <memory>
#include <vector>

#include "binary_tree_node.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"

using std::unique_ptr;
using std::vector;

vector<const unique_ptr<BinaryTreeNode<int>>*> CreateListOfLeaves(
    const unique_ptr<BinaryTreeNode<int>>& tree) {
  // Implement this placeholder.
  return {};
}

vector<int> CreateListOfLeavesWrapper(
    TimedExecutor& executor, const unique_ptr<BinaryTreeNode<int>>& tree) {
  auto result = executor.Run([&] { return CreateListOfLeaves(tree); });

  if (std::any_of(std::begin(result), std::end(result),
                  [](const unique_ptr<BinaryTreeNode<int>>*& x) {
                    return !x || !*x;
                  })) {
    throw TestFailure("Result list can't contain nullptr");
  }

  vector<int> extracted_result;
  for (const auto& x : result) {
    extracted_result.push_back(x->get()->data);
  }
  return extracted_result;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  // The timeout is set to 15 seconds for each test case.
  // If your program ends with TIMEOUT error, and you want to try longer time
  // limit, you can extend the limit by changing the following line.
  std::chrono::seconds timeout_seconds{15};

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "tree"};
  return GenericTestMain(args, timeout_seconds, "tree_connect_leaves.tsv",
                         &CreateListOfLeavesWrapper, DefaultComparator{},
                         param_names);
}
