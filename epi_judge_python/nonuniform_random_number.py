import collections
import functools
import math

from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


def nonuniform_random_number_generation(values, probabilities):
    # Implement this placeholder.
    return 0


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda : [nonuniform_random_number_generation(values, probabilities) for _ in range(N)])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


from sys import exit
from test_framework import generic_test, test_utils

if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(
            timeout_seconds, 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
