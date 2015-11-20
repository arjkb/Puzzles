
# AUTHOR	: Arjun Krishna Babu
# DATE		: Thu Nov 19 22:33:24 IST 2015
# OS		: openSUSE Leap 42.1

def	getSmallestWidth(i, j, width_array):
	smallest_width = 3 # 3 is the maximum possible width, according to question
	for index in range(i, j+1):
		if width_array[index] < smallest_width :
			smallest_width = width_array[index]
	return smallest_width


inp = input()
inp = [int(i) for i in inp.split()]

n = inp[0]	# length of the freeway
t = inp[1]	# number of testcases

width = input()
width = [int(i) for i in width.split()]

for i in range(t):
	testcase = input()
	testcase = [int(i) for i in testcase.split()]

	print(getSmallestWidth(testcase[0], testcase[1], width))
