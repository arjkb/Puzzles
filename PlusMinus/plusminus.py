# Given an array of integers, program finds the fraction of 
# positives, negatives, and zero

# Author: Arjun Krishna Babu
# Date	: 17 November 2015, Tuesday
# OS	: openSUSE Leap 42.1

def	getPosNegZero(numlist):
	pcount = 0
	ncount = 0
	zcount = 0

	for i in numlist:
		if i > 0:
			pcount += 1
		elif i < 0:
			ncount += 1
		elif i == 0:
			zcount += 1

	return pcount, ncount, zcount

n = int(input())
num_text = input()
numbers = [float(i) for i in num_text.split()]

counts = []
counts = getPosNegZero(numbers)

for c in counts:
	print("%.3f" %(float(c/n)))


