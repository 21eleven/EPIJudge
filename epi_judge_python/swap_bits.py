def swap_bits(x, i, j):
    # Implement this placeholder.
    if x >> i & 1 != x >> j & 1:
       x ^= 1 << i
       x ^= 1 << j
    return x


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('swap_bits.tsv', swap_bits)
