#Write a recursive python function to calculate sum of first N natural numbers

def calSum(n):
    if n==1:
        return 1
    return n+calSum(n-1)    
x=calSum(9)    
print("sum =",x)