#problem 1
#Answer 233168

def Multiples(Range):
	total = 0
	for i in range(1, Range +1):
		if i % 3 == 0 or i % 5 == 0: 
			total += i
	print(total)



Multiples(999)

