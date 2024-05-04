user_input = input().split(',')

multiples = []
for i in range(int(user_input[0])):
    multiples.append(int(user_input[1])*(i)) if int(user_input[1])*(i) not in multiples else None
    multiples.append(int(user_input[2])*(i)) if int(user_input[2])*(i) not in multiples else None

print(sorted(multiples)[int(user_input[0])])
