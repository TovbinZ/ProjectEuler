#problem 48
# Answer - 9110846700

def SelfPowers(num): 
	total = 0
	for i in range(num): 
		Number = i + 1
		result = Number ** Number 
		total += result
	print(total)

SelfPowers(10)


