#include <vector>

using std::vector;

bool MatrixSearch(const vector<vector<int>>& A, int x) {
  // Implement this placeholder.
  return true;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  generic_test_main(argc, argv, "search_row_col_sorted_matrix.tsv",
                    &MatrixSearch);
  return 0;
}
