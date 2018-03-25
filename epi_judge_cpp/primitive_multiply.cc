unsigned long Add(unsigned long a, unsigned long b) {
	short int carry = 0;
	unsigned long sum = 0;
	unsigned long place = 1;

	while ((a > 0) || (b > 0) || (carry > 0)) {
		if ((a & 1) && (b & 1)) {
			if (carry == 1) {
				sum ^=  place;
			} else {
				carry = 1;
			}
		} else if ((a & 1) || (b & 1)) {
			if (carry == 0) {
				sum ^= place;
			}
		} else {
			if (carry == 1) {
				sum ^= place;
				carry = 0;
			}
		}
		place <<= 1;
		a >>= 1;
		b >>= 1;
	}
	return sum;
}
		
				



unsigned long Multiply(unsigned long x, unsigned long y) {
  // Implement this placeholder.
  unsigned long product = 0;
  while (x) {
	  if (x & 1) {
		 product = Add(product, y);
	  }
  	  y <<= 1;
	  x >>= 1;
  }  
  return product;
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x", "y"};
  generic_test_main(argc, argv, param_names, "primitive_multiply.tsv",
                    &Multiply);
  return 0;
}
