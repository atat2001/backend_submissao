user_input = input()
counter = 0
acc = 0
for i in user_input:
    if i in user_input[counter::]:
        acc += list(user_input[counter+1::]).count(i)
    counter += 1
print(acc)