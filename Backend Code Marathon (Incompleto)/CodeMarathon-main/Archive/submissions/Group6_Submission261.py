value = int(input())
#11
#3
#1
k = 0
while (value - 11) >= 0:
    value -= 11
    k += 1
while (value - 3) >= 0:
    value -= 3
    k += 1
while (value - 1) >= 0:
    value -= 1
    k += 1

print(k)


