#Write a recursive python function to calculate sum of first N even natural numbers
def calEven(n):
    if n==1:
        return 2
    return (2*n)+calEven(n-1)    
x=calEven(4)    
print(x)