#problem 55
#Answer 249

def IsLychrel(Number): 

	global Lychrel
	Lychrel = ""
	def f(num,i):	
		Iterations = i 
		Iterations += 1 
		result = int(num) + int(str(num)[::-1])
		if Iterations == 50:
			global Lychrel
			Lychrel = "True"
		elif str(result) == str(result)[::-1]:
			return 
		else:
			f(result,Iterations) 	
	
	f(Number,0)
	if Lychrel == "True":
		return(True)
	else:
		return(False)
	
LychelList = []
for Number in range(10000):
	if IsLychrel(Number) == True:
		LychelList.append(Number)
		

print(len(LychelList))
	
