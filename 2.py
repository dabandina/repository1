import math 
 
a = int(input('Катет 1: ')) 
b = int(input('Катет 2: ')) 
S = (a*b)/2 
P = math.sqrt(a**2 + b**2) + a + b 
print(S) 
print(P)