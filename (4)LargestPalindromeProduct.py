# problem 4 
# Answer 906609

Answers = []

for Num1 in range(100,1000):
	for Num2 in range(100,1000): 
		Answers.append(Num1 * Num2)

Palindromes = []
for Answer in Answers: 
	if str(Answer)[::-1] == str(Answer):
		Palindromes.append(Answer)
Palindromes.sort()
print(Palindromes)
