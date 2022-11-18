#problem 40
#Answer 210


Decimal ="."
for i in range(250000):
	Num = i +1
	Decimal += str(Num)
	


Answer = int(Decimal[1]) * int(Decimal[10]) * int(Decimal[100]) * int(Decimal[1000]) * int(Decimal[10000]) * int(Decimal[100000]) * int(Decimal[1000000])


#print(int(Decimal[1]))
#print(int(Decimal[10]))
#print(int(Decimal[100]))
#print(int(Decimal[1000]))
#print(int(Decimal[10000]))
#print(int(Decimal[100000]))
#print(int(Decimal[1000000]))


print()
