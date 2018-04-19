def reverse(x):
	# Implement this placeholder.
	result = 0
	neg = False 
	if x < 0:
		neg = True
		x *= -1
	while x:
		result = result * 10 + x % 10
		x//= 10
	if neg == True:
		result *= -1
	return result
	

from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('reverse_digits.tsv', reverse)
