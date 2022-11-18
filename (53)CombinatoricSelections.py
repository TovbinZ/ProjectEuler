# problem 53
# Answer - 4075

import math
factorial = math.factorial

def Choose(n,r):
	Answer = (factorial(n))/(factorial(r)*(factorial(n-r)))
	return Answer

total = 0
for n in range(1,101):
	for r in range(1,101):
		if r > n: 
			pass
		else:
			if Choose(n,r) > 1000000:
				total += 1
print(total)