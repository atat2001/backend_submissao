user_input = input()


user_input = int(user_input)

count = 0
for i in range(1, user_input + 1):
    s = str(i)
    for j in s:
        if j == "0" or j == "1":
            count += 1

print(count)
