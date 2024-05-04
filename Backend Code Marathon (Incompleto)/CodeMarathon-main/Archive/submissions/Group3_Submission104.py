user_input = input().split(',')
print(user_input)
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])

print(user_input)


nrs = [user_input[1]] + [user_input[2]]

lista_mult = []
for i in range(1,user_input[0]+1):
    lista_mult += [int(nrs[0])* i]
    lista_mult += [int(nrs[1]) * i]

lista_mult.sort()

output = lista_mult[nrs[0]]
print(lista_mult)







print(output)