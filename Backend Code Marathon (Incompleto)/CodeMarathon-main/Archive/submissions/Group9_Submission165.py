n = int(input())

sum = 0

for i in range(1, n+1):
    a = str(i)
    for b in a:
        if b == '1' or b == '0':
            sum += 1

print(sum)