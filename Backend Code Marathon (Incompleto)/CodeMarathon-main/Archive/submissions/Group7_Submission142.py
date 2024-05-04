user_input = input().split(',')

multiples = []
for i in range(int(user_input[0])):
    multiples.append(int(user_input[1])*(i+1)) if int(user_input[1])*(i+1) not in multiples else None
    multiples.append(int(user_input[2])*(i+1)) if int(user_input[2])*(i+1) not in multiples else None

print(sorted(multiples)[int(user_input[0])-1])
