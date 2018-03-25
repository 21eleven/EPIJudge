def divide(x, y):
    # Implement this placeholder.
    result = 0
    power = 32
    while x >= y:
        while y << power > x:
            power -= 1
        result += 1 << power
        x -= y << power
    return result


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("primitive_divide.tsv", divide)
