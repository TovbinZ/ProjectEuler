#problem 17
#21123


def Ones(num):
	words = ["one","two","three","four","five","six","seven","eight","nine"]
	return words[num-1]
def Teens(num):
	words = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	return words[num]
def Tens(num):
	words = ['twenty',"thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	return words[num - 2]


def DoIt(num):
	if len(str(num)) == 1:
		return f"{Ones(num)}"
	if len(str(num)) == 2:
		if num in [10,11,12,13,14,15,16,17,18,19]:
			return f"{Teens(num % 10)}"
		else:
			if int(num % 10) == 0:
				return f"{Tens(int(num/10))}"
			else:
				tensdigit = int(num / 10)
				onesdigit = num % 10
				return f"{Tens(tensdigit)} {(Ones(onesdigit))}"
	else:
		if int(num % 100) == 0:
			return f"{Ones(int(num / 100))} hundred"
		else:
			return f"{Ones(int(num / 100))} hundred and {DoIt(num % 100)}"

total = 0
for i in range(1,1000):
	total += len(DoIt(i).replace(" ",""))
	# print(DoIt(i))

thousand = "onethousand"

total += len(thousand)

print(total)
