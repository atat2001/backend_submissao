rad = int(input())
sum = 0
while (rad > 0):
    if (rad - 11 >= 0):
        rad -= 11
        sum += 1
    elif (rad - 3 >= 0):
        rad -= 3
        sum += 1
    elif (rad - 1 >= 0):
        rad -= 1
        sum += 1

print(sum)