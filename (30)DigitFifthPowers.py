# Problem 30
# Answer - 443839


Same = []

for number in range(2,1000000):
	total = 0
	for digit in str(number):
		total += int(digit)**5
	if total == number:
		Same.append(number)

Answer = 0
for Number in Same:
	Answer += Number
print(Answer) 


