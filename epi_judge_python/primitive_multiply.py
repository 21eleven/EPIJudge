def add(a, b):
    s = 0
    carry = 0
    place = 1
    while (a > 0) or (b > 0) or (carry > 0):
        if (a & 1) & (b & 1):
            if carry == 1:
                s ^= place
                place <<= 1
            else:
                carry ^= 1
                place <<= 1
        elif (a & 1) | (b & 1):
            if carry == 1:
                place <<= 1
            else:
                s ^= place
                place <<= 1
        else:
            if carry == 1:
                s ^= place
                carry = 0
                place <<= 1
            else:
                place <<= 1
        a >>= 1
        b >>= 1
    return s

def add2(a, b):
    s, carryin, k, temp_a, temp_b = 0,0,1,a,b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        s |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k <<= 1
        temp_a, temp_b = temp_a >> 1, temp_b >> 1
    return s | carryin

def multiply(x, y):
    # Implement this placeholder.

    result = 0
    while x:
        if x & 1:
            result = add(result, y)
        x >>= 1
        y <<= 1
    return result


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('primitive_multiply.tsv',
                                              multiply)
