#problem 52
#Answer - 142857



def MakeList(Num): 
	numList = []
	for digit in str(Num):
		numList.append(digit)
	numList.sort()
	return numList



def Test(Num): 
	Number = MakeList(Num)

	if MakeList(Num*2) == Number:
		if MakeList(Num*3) == Number:
			if MakeList(Num*4) == Number:
				if MakeList(Num*5) == Number: 
					if MakeList(Num*6) == Number: 
						print(Num)



for i in range(10000,1000000):
	Test(i)


