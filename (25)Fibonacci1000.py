#problem 25
#Answer 4782 


# import sys
# sys.set_int_max_str_digits(1000000)

Repeat = True
FibonacciList = [1,1]
index = 2
while Repeat:
	num1 = FibonacciList[-2]
	num2 = FibonacciList[-1]
	FibonacciList.append(num1 + num2)
	result = FibonacciList[-1]
	index += 1
	if len(str(result)) >= 1000:
		Repeat = False
		print(index)
