#Write a recursive python function to calculate sum of first N odd natural numbers

def calOdd(n):
    if n==0:
        return 0
    return (2*n-1)+calOdd(n-1)    
x=calOdd(6)    
print(x)