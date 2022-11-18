# problem 10
# Answer - 142913828922
from sympy import ntheory


total = 0

for i in range(2000000): 
    if ntheory.primetest.isprime(i) == True: 
        total += i

print(total)