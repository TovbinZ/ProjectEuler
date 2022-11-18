

#problem 13
#Answer 5537376230

f = open("Nums.txt", "r")
NumList = f.readlines()


print(len(NumList))



total = 0

for i in NumList: 
	total += int(i)

print(total)