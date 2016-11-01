import sys

def factorial(n):
    if n != 1:
        return n * factorial(n - 1)
    else:
        return n
    
    
    
    
    
    
print(factorial(int(input())))