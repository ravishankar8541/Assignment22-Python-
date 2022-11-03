"""Write a recursive python function to calculate sum of squares of first N natural
numbers"""
def sumOfSquare(n):
    if n==1:
        return 1
    return (n*n)+sumOfSquare(n-1)
x=sumOfSquare(3) 
print(x)       