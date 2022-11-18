#problem 6 
# Answer 25164150


def SumSquares(Num): 
	result = 0
	for i in range(Num):
		Number = i + 1
		result += Number ** 2
	return(result)


# SumSquares(10)




def SquareSum(Num): 
	result = 0
	for i in range(Num):
		Number = i + 1
		result += Number
	return(result ** 2)




print(SquareSum(100) - SumSquares(100))