def closest_int_same_bit_count(x):
    # Implement this placeholder.
    for i in range(64-1):
        if (x >> i & 1) != (x >> (i+1) & 1):
            x^= 1 << i
            x ^= 1 << i+1
            return x


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("closest_int_same_weight.tsv",
                                              closest_int_same_bit_count)
