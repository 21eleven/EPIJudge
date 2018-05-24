import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def eval_dim(d1,d2):
	pts1 = [d1[0], d1[0]+d1[1]]
	pts2 = [d2[0], d2[0]+d2[1]]
	if (pts1[0] <= pts2[1] <= pts1[1]) or (pts2[0] <= pts1[1] <= pts2[1]): #then there is intersection
		side = pts1 + pts2
		side.sort()
		return (side[1], side[2]-side[1])
	else:
		return (0,-1)

def intersect_rectangle(R1, R2):
	# Implement this placeholder.
	y, height = eval_dim((R1[1],R1[3]), (R2[1],R2[3]))
	x, width = eval_dim((R1[0],R1[2]), (R2[0],R2[2]))
	if height < 0 or width < 0:
		x, y, width, height = 0,0,-1,-1
	return Rectangle(x, y, width, height)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(expected, result):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    return fmt(expected), fmt(result)


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'rectangle_intersection.tsv',
        intersect_rectangle_wrapper,
        res_printer=res_printer)
