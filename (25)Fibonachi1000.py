#problem 25
#Answer 4782 


def Fibonacci(amount,index): 
	FibonacciList = [1,1] 
	for i in range(int(amount) - 2): 
		num1 = FibonacciList[-2]
		num2 = FibonacciList[-1]
		FibonacciList.append(num1 + num2)
		result = FibonacciList[-1]
		print("{}:{}:{}".format(index,result,len(str(result))))
		index += 1
		





Fibonacci(12,3)