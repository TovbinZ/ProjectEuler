

#Problem 7
# Answer 104743

import sys

sys.setrecursionlimit(10**6)


def IsPrime(Num):
	DivisibleList = []
	for i in range(Num): 
		Divisor = i + 1
		if Num % Divisor == 0:
			DivisibleList.append(Divisor)
	if len(DivisibleList) == 2: 
		return(True)
	elif len(DivisibleList) == 1: 
		return(True)
	else: 
		return(False)



def ThousandthPrime(Amount,Number,PrimeList):
	PrimeList = list(PrimeList)
	if len(PrimeList) != Amount + 1:
		if IsPrime(Number) == True: 
			PrimeList.append(Number)
			ThousandthPrime(Amount,Number + 1,PrimeList)
		else:
			ThousandthPrime(Amount,Number + 1,PrimeList)
	else: 
		print(PrimeList[-1])






ThousandthPrime(100,1,[])







