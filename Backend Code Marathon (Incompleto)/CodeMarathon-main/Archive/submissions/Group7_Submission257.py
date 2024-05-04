def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result

user_input = input()
input = user_input.split(" ")
casas = input[0].split(",")
acasas = input[1].split(",")
temp = 0

for acasa in acasas:
    for casa in casas:
        if distance(acasa,casa) > temp:
            temp = distance(acasa,casa)
print(temp)