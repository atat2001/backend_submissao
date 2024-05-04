user_input = input()

arr = []
for u in user_input:
    arr.append(int(u))

count = 0
for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
        if arr[i] == arr[j]:
            count += 1
            break

print(count)
