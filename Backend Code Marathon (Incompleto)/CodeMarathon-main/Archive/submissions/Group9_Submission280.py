pos = input().split(',')

prev = 0

result = []

for i, el in enumerate(pos):
    if el[-2] == 'P':
        prev = int(el[:-3])
    elif abs(int(el[:-3]) - prev) >= 10 and el[-2] == 'N':
        result += [i+1]
        prev = int(el[:-3])

print(result)
    