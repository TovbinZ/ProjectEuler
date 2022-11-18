#problem 20
# Answer 648

input_num = int(input("Input a Number: "))
num = input_num - 1 

output = 0
for i in range(num): 
    output = input_num * (num - i)
    # print(f"{input_num} times {num - i} is {output}" )
    input_num = output 

total = 0
for i in str(output): 
    total += int(i)

    



print(total)