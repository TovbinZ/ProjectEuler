# Problem 29
# Answer - 9183

Numbers = []
for a in range(2,101): 
	for b in range(2,101):
		Numbers.append(a**b)

Distinct = list(dict.fromkeys(Numbers))
print(len(Distinct))


