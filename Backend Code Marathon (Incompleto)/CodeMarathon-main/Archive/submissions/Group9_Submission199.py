n = input()

par = 0

for i in range(len(n)):
    for j in range(i, len(n)):
        if n[i] == n[j] and i < j:
            par += 1

print(par)