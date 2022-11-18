# problem 5
# Answer 232792560

#range is between 100 million and 1 billion

for Candidate in range(100000000,1000000000,10): 
	DivibleBy = 0
	for i in range(20): 
		Num = i+1 
		if Candidate%Num == 0: 
			DivibleBy +=1
		
	if DivibleBy == 20: 
		print(Candidate)
	






