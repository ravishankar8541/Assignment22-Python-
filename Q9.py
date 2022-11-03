# Write a recursive python function to print octal of a given decimal number
def conInOct(n):
    if n==1:
        print("1",end="")
    else:
        conInOct(n//8)
        print(n%8)    
conInOct(12)        