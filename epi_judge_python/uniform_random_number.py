import functools
import random

from test_framework.random_sequence_checker import check_sequence_is_uniformly_random, run_func_with_retries
from test_framework.test_utils import enable_timer_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound, upper_bound):
	_range = upper_bound - lower_bound + 1
	flips = 0
	while 2**flips < _range:
		flips += 1
	dist_range = 2**flips
	reject = dist_range - _range
	bits = flips
	out_of_bounds = True
	while out_of_bounds:
		bitstring = ''
		for _ in range(bits):
			bitstring += str(zero_one_random())
		value = int(bitstring,2)
		if value < (dist_range - reject):
			out_of_bounds = False

	return value

def uniform_random1(lower_bound, upper_bound):
	outcomes = upper_bound - lower_bound + 1
	while True:
		i = 0
		result = 0
		while (1 << i) < outcomes:
			result = (result << 1) | zero_one_random()
			i += 1
		if result < outcomes:
			break
	return result + lower_bound


@enable_timer_hook
def uniform_random_wrapper(timer, lower_bound, upper_bound):
    def uniform_random_runner(timer, lower_bound, upper_bound):
        timer.start()
        result = [
            uniform_random(lower_bound, upper_bound) for _ in range(100000)
        ]
        timer.stop()

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, timer, lower_bound,
                          upper_bound))


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('uniform_random_number.tsv',
                                              uniform_random_wrapper)
