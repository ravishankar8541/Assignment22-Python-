#Write a recursive python function to calculate the factorial of a number.
def calFact(n):
    if n==0:
        return 1
    return (n*calFact(n-1))  
x=int(input("Enter a number :"))    
bag=calFact(x)
print("factorial of ",x,"is",bag)
