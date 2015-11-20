# You're given an integer N. 
# WAP to calculate the sum of all the digits of N

def getSum(number):
    sum = 0
    while number > 0 :
        dig = number % 10
        sum += dig
        number /= 10

    return sum

nums = []
t = int(input())
for i in range(t):
    nums.append(int(input()))
for i in nums:
    print(int(getSum(i)))
print("")
