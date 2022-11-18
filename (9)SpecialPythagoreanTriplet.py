# problem 9 
# Answer - 31875000

import math

Squares = []
for Num in range(1000):
	Squares.append(Num**2) 


Groups = []

for Num1 in range(1,1000):
	for Num2 in range(1,1000):
		ABC2 = []
		ABC2.append(Num1)
		ABC2.append(Num2)
		ABC2.append(Num1**2 + Num2**2)
		Groups.append(ABC2)

		

EditedGroups = []

for Group in Groups: 
	if Group[2] in Squares:
		EditedGroups.append(Group)


Answer = []

for Group in EditedGroups: 
	if (Group[0] + Group[1] + math.sqrt(Group[2])) == 1000:
		Answer.append(Group)
		

RealAnswer = Answer[0][0] * Answer[0][1] * math.sqrt(Answer[0][2])
print(RealAnswer)
