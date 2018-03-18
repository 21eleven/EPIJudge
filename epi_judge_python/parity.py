def parity(x):
    # Implement this placeholder.
    parity = 0
    while x:
        parity ^= 1
        x &= x - 1
    return parity


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('parity.tsv', parity)
