#problem 2
#Answer 4613732

def Fibonacci(amount,index): 
	FibonacciList = [1,1] 
	for i in range(int(amount) - 2): 
		num1 = FibonacciList[-2]
		num2 = FibonacciList[-1]
		FibonacciList.append(num1 + num2)
		result = FibonacciList[-1]
		# print("{}:{}".format(index,result))
		index += 1
	return(FibonacciList)
		




EvenFibanacci = 0
for i in Fibonacci(33,3): 
	if i % 2 == 0: 
		EvenFibanacci += i


# Fibonacci(33,33)

print(EvenFibanacci)