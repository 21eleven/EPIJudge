#include <deque>
#include <vector>

using std::deque;
using std::vector;

int MaxSquareSubmatrix(const vector<deque<bool>>& A) {
  // Implement this placeholder.
  return 0;
}

#include "test_framework/generic_test.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  GenericTestMain(args, "max_square_submatrix.tsv", &MaxSquareSubmatrix,
                  DefaultComparator{}, param_names);
  return 0;
}
