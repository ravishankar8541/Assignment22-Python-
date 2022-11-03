#  Write a recursive python function to calculate sum of the digits of a given number

def sumOfDigit(n):
    if n==0:
        return 0
    return ((n%10)+sumOfDigit(n//10))
print(sumOfDigit(145))       