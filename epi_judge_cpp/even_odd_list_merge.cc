
#include "list_node.h"

shared_ptr<ListNode<int>> EvenOddMerge(const shared_ptr<ListNode<int>>& L) {
  // Implement this placeholder.
  return nullptr;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L"};
  GenericTestMain(args, "even_odd_list_merge.tsv", &EvenOddMerge,
                  DefaultComparator{}, param_names);
  return 0;
}
