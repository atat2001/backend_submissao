user_input = input()

arr = []
for n in user_input.split(","):
    arr.append(int(n))


count = 0
for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
        count += arr[i]

if arr[0] > arr[1]:
    count += arr[0]

if arr[len(arr) - 1] > arr[len(arr) - 2]:
    count += arr[len(arr) - 1]

print(count)
