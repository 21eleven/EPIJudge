#include <map>
#include <iostream>
using namespace std;

unsigned long swap(unsigned long x, int i, int j) {
  if (((x >> i) & 1) != ((x >> j) & 1)) {
     x ^= 1 << i;
     x ^= 1 << j;
  }
  return x;
}

map <long, long> lookup;

int populateLookup() {
	for ( long x = 0; x < 65536; x++ ) {
		long rev = x;
		for ( int i = 0; i < 8; i++ ) {
			rev = swap(rev, i, 15 - i);
		}
		lookup.insert(pair <long, long> (x, rev));
	}
	return 0;
}

unsigned long ReverseBits(unsigned long x) {
  // Implement this placeholder.
  populateLookup();
  return lookup.find(x >> 48);
}

#include "test_framework/test_utils_generic_main.h"

int main(int argc, char* argv[]) {
  std::vector<std::string> param_names{"x"};
  generic_test_main(argc, argv, param_names, "reverse_bits.tsv", &ReverseBits);
  return 0;
}
