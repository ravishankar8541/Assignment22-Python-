#Write a recursive python function to print binary of a given decimal number.
def conInBin(n):
    if n==1:
     print("1",end="")
    else: 
     conInBin(n//2)   
     print(n%2,end="")  
conInBin(4)