user_input = input()
input = user_input.split(",")
acc = []
for i in input[1]:
    if len(acc) == 0:
        acc.append(i)
    elif len(acc) > 0 and i != acc[len(acc)-1]:
        acc.append(i)
acc = "".join(acc)
if acc == input[0]:
    print("true")
else:
    print("false")