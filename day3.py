import sys

N = int(input(":").strip())

if N % 2 != 0:
    print("Weird")
    
elif N % 2 == 0 & 2 <= N <=5:
    print("Not Weird")
    
elif N % 2 == 0 & 6 <= N <= 20:
    print("Weird")
    
elif N >= 20 & N % 2 == 0:
    print("Not Weird")
    
else:
    print("Its broke")
    
print( 24 % 2)