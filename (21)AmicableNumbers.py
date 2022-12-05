#problem 21
# 31626


def d(n): 
	ProperDivisors = []
	for Devisor in range(n - 1): 
		Devisor += 1
		if n % Devisor == 0: 
			ProperDivisors.append(Devisor)
	total = 0
	for Devisor in ProperDivisors: 
		total += Devisor
	return total
	


total = 0
for i in range(10000):
	if d(i) != i:
		if i == d(d(i)):
			total += i
	


print(total)