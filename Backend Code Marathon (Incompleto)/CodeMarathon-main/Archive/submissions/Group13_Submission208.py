string = input("")
res = 0
for i in range(len(string) - 1):
    for j in range (i + 1, len(string)):
        if (string[i] == string[j]):
            res += 1
print(res) 