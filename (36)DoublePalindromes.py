#problem 36
#Answer 872187

def Palindromes(Num):
	if str(Num) == str(Num)[::-1]:
		Binary = str(bin(Num)[2::])
		if Binary == Binary[::-1]:
			return(True)
		else:
			return(False)
	else: 
		return(False)
		
		
		

PalindromeList = []		
for Number in range(1000000):
	if Palindromes(Number) == True:
		PalindromeList.append(Number)
		
		
print(sum(PalindromeList))	
