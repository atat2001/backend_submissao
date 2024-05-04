user_input = input()

arr = []
for u in user_input:
    arr.append(int(u))

resulting = len(arr) - 1

i = 0
while i > len(arr):
    i = arr[i]

print(i == resulting)
