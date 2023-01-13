#problem 22
#Answer 871198282
f = open("Names.txt","r")
Names = f.read()
NamesList = Names.split(",")
NamesList.sort()




def Score(Name):
	NewName = Name.replace('"','')
	NewName2 = NewName.replace('\n','')
	Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	Result = 0
	for letter in NewName2: 
		Result += int(Alphabet.index(letter)) + 1
	
	return(Result * (int(NamesList.index(Name)) + 1))
	



Answer = 0
for Name in NamesList:
	Answer += int(Score(Name))
	

print(Answer)
