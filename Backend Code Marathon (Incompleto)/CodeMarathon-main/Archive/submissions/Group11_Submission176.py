user_input = input()

arr = []
for u in user_input:
    arr.append(int(u))

left_index = 0
right_index = len(arr) - 1
count = 0
for i in range(len(arr)):
    if arr[i] >= arr[left_index]:
        minn = min(arr[i], arr[left_index])
        other = arr[left_index + 1 : i]
        if arr[left_index] > 0:
            for n in range(len(other)):
                count += minn - other[n]
        left_index = i

for i in range(len(arr) - 1, 0, -1):
    if arr[i] >= arr[right_index]:
        minn = min(arr[i], arr[right_index])
        other = arr[i + 1 : right_index]
        if arr[right_index] > 0:
            for n in range(len(other)):
                count += minn - other[n]
        right_index = i
print(count)
