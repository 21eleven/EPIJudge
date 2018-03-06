import functools

from test_framework.test_utils import enable_executor_hook


# Assumes node_to_delete is not tail.
def deletion_from_list(node_to_delete):
    # Implement this placeholder.
    return


@enable_executor_hook
def deletion_from_list_wrapper(executor, head, node_to_delete_idx):
    node_to_delete = head
    if node_to_delete is None:
        raise RuntimeError('List is empty')
    for _ in range(node_to_delete_idx):
        if node_to_delete.next is None:
            raise RuntimeError("Can't delete last node")
        node_to_delete = node_to_delete.next

    executor.run(functools.partial(deletion_from_list, node_to_delete))

    return head


from sys import exit
from test_framework import generic_test, test_utils

if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(timeout_seconds,
                                       'delete_node_from_list.tsv',
                                       deletion_from_list_wrapper))
