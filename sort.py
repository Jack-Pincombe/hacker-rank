def induction(x):
    y = x + 1
    
    x *= y
    
    x/=2
    
    print(x)
    
    

def recursion(x):
    assert x > 0
    print(x)
    
    if x == 1:
        print(0)
        
    else:
        x -= 1
        recursion(x)
        
    
def factorial(x):
    assert x > 0
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
    
    
def sumOddNumbers(n):
    assert n > 0
    if n == 1:
        return 1
    else: 
        return ((n * 2) - 1) + sumOddNumbers(n - 1)
        

    
def oddTotal(x):
    
    # x is the total number of numbers
    
    if x == 1:
        return x
    else:
        return ((x *2) - 1) + oddTotal(x -1)

print(oddTotal(5))