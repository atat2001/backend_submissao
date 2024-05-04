numbers = list(map(int, input()))

result = 0
for x, number in enumerate(numbers):
    for y in range(x, len(numbers)):
        if y > x and number == numbers[y]:
            result += 1
print(result)
