n = int(input())

sum = 0

for i in range(1, n+1):
    b = str(bin(i))[2:]
    #print(b)
    sum += len(b)

print(b)