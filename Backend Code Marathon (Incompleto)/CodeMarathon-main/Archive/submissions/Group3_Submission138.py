user_input = input().split(',')

for i in range(len(user_input)):
    user_input[i] = int(user_input[i])




nrs = [user_input[1]] + [user_input[2]]

lista_mult = []
for i in range(1,1000):
    if int(nrs[0])* i not in lista_mult:
        lista_mult += [int(nrs[0])* i]
    if int(nrs[1])* i not in lista_mult:
        lista_mult += [int(nrs[1]) * i]

lista_mult.sort()

output = lista_mult[int(user_input[0])-1]








print(output)