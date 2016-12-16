def induction(x):
    y = x + 1
    
    x *= y
    
    x/=2
    
    print(x)
    
    

def recursion(x):
    print(x)
    
    if x == 1:
        print(0)
        
    else:
        x -= 1
        recursion(x)
        
    
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
    
    

print(factorial(10))