# Program to find the sum of the elements of an array

def getSum(numList):
	sum = 0
	for num in numList:
		sum += num
	return sum

n = int(input())
x = input()
x = [int(i) for i in x.split()] # convert string to list of integers

print(getSum(x))
