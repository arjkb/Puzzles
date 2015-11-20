# Find the largest decent number having D digits
# Decent number has the following properties:
#	- 3, 5, or both its digits. No other digit is allowed.
# 	- Number of times 3 appears is divisible by 5
#	- Number of times 5 appears is divisible by 3


# AUTHOR	: Arjun Krishna Babu
# DATE		: Thu Nov 19 10:06:19 IST 2015
# OS		: openSUSE Leap 42.1



def generateNum(m, n):
	return int('5'*m + '3'*n)
	
def getMaxCombo(number):
	m = 0 # number of 5
	n = 0 # number of 3
	for n in range(number + 1):
		m = number - n
		#print("Debug: ( ", m, ", ", n, ")")
		if m % 3 == 0 :
			if n % 5 == 0 :
				return m
		
	return -1

t = int(input())

for i in range(t):
	d = int(input()) # get the number of digits
	count_5 = getMaxCombo(d)
	#print(count_5)
	if count_5 == -1 :
		print("-1")
	else :
		print(generateNum(count_5, d - count_5))
