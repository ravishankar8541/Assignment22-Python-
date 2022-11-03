#Write a recursive python function to calculate sum of cubes of first N natural numbers

def sumOfCube(n):
    if n==1:
        return 1
    return (n**3)+sumOfCube(n-1)
x=sumOfCube(3) 
print(x)    