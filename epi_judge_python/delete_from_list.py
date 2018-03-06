import functools

from test_framework.test_utils import enable_executor_hook


# Delete the node past this one. Assume node is not a tail.
def delete_after(node):
    # Implement this placeholder.
    return


@enable_executor_hook
def delete_from_list_wrapper(executor, head, node_idx):
    node_to_delete = head
    prev = None
    if node_to_delete is None:
        raise RuntimeError('List is empty')
    for _ in range(node_idx):
        if node_to_delete.next is None:
            raise RuntimeError("Can't delete last node")
        prev = node_to_delete
        node_to_delete = node_to_delete.next

    executor.run(functools.partial(delete_after, prev))

    return head


from sys import exit
from test_framework import generic_test, test_utils

if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(timeout_seconds, 'delete_from_list.tsv',
                                       delete_from_list_wrapper))
