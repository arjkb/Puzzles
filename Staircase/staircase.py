# Given an integer N, draw a staircase using spaces and '#'

# AUTHOR	: Arjun Krishna Babu
# DATE		: Tue Nov 17 22:54:04 IST 2015
# OS		: openSUSE Leap 42.1

def drawSymbol(symbol, count):
	for i in range(count):
		print(symbol, end="")

n = int(input())


for i in range(n):
	drawSymbol(" ", n - i - 1)
	drawSymbol("#", i + 1)
	print()
