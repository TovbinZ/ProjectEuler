
# Problem 3
# Answer - 6857

from sympy import ntheory 


result = ntheory.primetest.isprime(7)
print(result)


primes = []


for i in range(1000000): 
    if ntheory.primetest.isprime(i) == True: 
        primes.append(i)


primeFactors = []
for prime in primes: 
    if 600851475143 % prime == 0: 
        primeFactors.append([prime])


print(primeFactors)

