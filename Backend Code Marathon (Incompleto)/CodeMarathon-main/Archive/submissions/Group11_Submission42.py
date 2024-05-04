user_input = input()

arr = []
for u in user_input:
    if u != ",":
        arr.append(int(u))


index = arr[0]
other = []
for i in range(1, index):
    for j in range(1, len(arr)):
        other.append(arr[j] * i)

other.sort()


print(other[index - 1])

# 2 3 4
