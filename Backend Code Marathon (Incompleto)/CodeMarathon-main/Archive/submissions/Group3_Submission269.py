user_input = input()

correta, s = user_input.split(",")
teste = [c for c in s]

for c in correta:
    encontrou = False
    for e in teste.copy():
        if encontrou and e!=c:
            break
        if e == c:
            teste.remove(c)
            encontrou = True
    else:
        break

if teste == []:
    print("true")
else:
    print("false")