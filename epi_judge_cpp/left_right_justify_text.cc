#include <string>
#include <vector>

using std::string;
using std::vector;

vector<string> JustifyText(const vector<string>& words, int L) {
  // Implement this placeholder.
  return {};
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"words", "L"};
  GenericTestMain(args, "left_right_justify_text.tsv", &JustifyText,
                  DefaultComparator{}, param_names);
  return 0;
}
