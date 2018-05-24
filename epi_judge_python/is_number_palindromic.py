def is_palindrome_number(x):
	# Implement this placeholder.
	if x < 0 : return False
	if x == 0: return True
	upper = 100000000000000000000
	lower = 10
	#upper_check, lower_check = x, x
	while x//upper==0:
		upper//=10
	while upper*10 >= lower:
		if ((x//upper)%10 != (x%lower)//(lower//10)):
		#if x//upper != x%lower:
			return False
		upper//=10
		lower*=10
	return True

"""import math

def is_palindrome_number(x):
	if x <= 0:
		return x == 0
	num_digits = math.floor(math.log10(x)) + 1
	msd_mask = 10**(num_digits -1)
	for i in range(num_digits // 2):
		if x // msd_mask != x% 10:
			return False
		x %= msd_mask
		x //= 10
		msd_mask //= 100
	return True

def is_palindrome_number(x):
	if x <= 0:
		return x == 0
	upper = 10**math.floor(math.log10(x))
	lower = 10
	while upper*10 >= lower:
		if ((x//upper)%10 != (x%lower)//(lower//10)):
			return False
		upper//=10
		lower*=10
	return True
"""	


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("is_number_palindromic.tsv",
                                              is_palindrome_number)
