#problem 14
# 837799


def length(n,count):
    if(n == 1):
       return count
    else:
        if(n % 2 == 0):
            return length(n/2, count + 1)
        else:
            return length(3*n + 1, count + 1)



past = 0
answer = 0
for x in range(1,1000000):
    currentlength = length(x,1)
    if(currentlength > past):
        past = currentlength
        answer = x





print(answer)