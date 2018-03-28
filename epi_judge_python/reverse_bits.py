def reverse_bits(x):
    # Implement this placeholder.
    #lookup = init_look_up()
    return (lookup[x&0xFFFF] << 48)^(lookup[x>>16&0xFFFF] << 32)^(lookup[x>>32&0xFFFF] << 16)^(lookup[x>>48]) 

def init_look_up():
    d = {}
    for x in range(0xFFFF+1):
       rev = x
       for i in range(8):
          rev = swap(rev,0+i,15-i)
       d[x]=rev
    return d


def swap(x,i,j):
    if (x>>i)&1 != (x>>j)&1:
       x ^= 1<<i
       x ^= 1<<j
    return x
lookup = init_look_up()

from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("reverse_bits.tsv", reverse_bits)
