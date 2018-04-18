def power(x, y):
	# recursive example
	if y < 0:			# negative exponent
		y *= -1
		x = 1/x
	if y == 0:			# if exponent is zero return 1
		return 1
	if y == 1:			# if exponent is one return x
		return x
	if y == 2:			
		return x * x
	elif y & 1:
		p = power(x , y -1 )
		return x * p
	else:
		p = power(x, y >> 1)
		return p * p
"""
def power(x, y):
	# book implementation, this is marginally faster
	result, power = 1.0, y
	if y < 0:
		power *= -1
		x = 1/x
	while power:
		if power & 1:
			result *= x
		power, x = power >> 1, x*x
	return result
"""


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main('power_x_y.tsv', power)
