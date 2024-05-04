number = int(input())


def count(number):
    total = 0
    for i in str(number):
        if i == '0' or i == '1':
            total += 1
    return total


total = 0
for i in range(number, 0, -1):
    total += count(i)
print(total)
