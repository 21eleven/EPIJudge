from sys import exit

from list_node import ListNode
from test_framework import generic_test, test_utils


def cyclically_right_shift_list(L, k):
    # Implement this placeholder.
    return None


if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(timeout_seconds,
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
