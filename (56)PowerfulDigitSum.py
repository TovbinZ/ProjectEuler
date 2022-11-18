# problem 56 
# Answer  - 972


Answers = []
for Num1 in range(1,100): 
	for Num2 in range(1,100):
		Answers.append(Num1**Num2)

Totals = []
for Answer in Answers: 
	total = 0
	for digit in str(Answer): 
		total += int(digit)
	Totals.append(total)



Totals.sort()

print(Totals)