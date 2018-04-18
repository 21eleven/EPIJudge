
unsigned long ClosestIntSameBitCount(unsigned long x) {
  // Implement this placeholder.
  int limit = 64;
  int i = 0;
  while (i < limit) {
    // if ((x & (1 << i)) != ((x & (1 << i + 1))>> 1)) {
    if (((x >> i) & 1) != ((x >> i+1) & 1)) {
       x ^=  (1 << i);
       x ^= (1 << i+1);
       return x;
    }
    i++; 
  }
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x"};
  generic_test_main(argc, argv, param_names, "closest_int_same_weight.tsv",
                    &ClosestIntSameBitCount);
  return 0;
}
