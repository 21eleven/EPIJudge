from sys import exit

from bst_node import BstNode
from test_framework import generic_test, test_utils


def rebuild_bst_from_preorder(preorder_sequence):
    # Implement this placeholder.
    return None


if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(timeout_seconds,
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
