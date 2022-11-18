# problem 12
# Answer 76576500

def TriangleNum(Range):
	result = 0 
	for i in range(Range):
		num = i+1
		result += num
	return(result)
		
		


def Divibles(Num):
	DivisibleList = []
	for i in range(Num): 
		Divisor = i + 1
		if Num % Divisor == 0:
			DivisibleList.append(Divisor)
	return(len(DivisibleList))
	


#print(Divibles(TriangleNum(12375)))


print(TriangleNum(12375))
