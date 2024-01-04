#Problem 112
#Answer 1587000
def NumberType(num):
	numstring = str(num)

	D = 0
	I = 0

	for i in range(len(numstring) - 1):
		if i != len(numstring):
			if int(numstring[i]) > int(numstring[i + 1]):
				D += 1
			elif int(numstring[i]) < int(numstring[i + 1]):
				I += 1
	if D == 0 and I > 0:
		return "Increasing"
	if I == 0 and D > 0:
		return "Decreasing"
	elif D > 0 and I > 0:
		return "Bouncing"

def Percentage(num):

	Total = 0
	for i in range(num+1):
		if NumberType(i) == "Bouncing":
			Total += 1

	return (Total/num) * 100



print(Percentage(1587000))



