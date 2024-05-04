user_input = input()

arr = []
for u in user_input:
    if u != ",":
        arr.append(int(u))

index = arr[0]
other = []
for i in range(1, index):
    first = arr[1] * i
    second = arr[2] * i
    if first not in other:
        other.append(arr[1] * i)
    if second not in other:
        other.append(arr[2] * i)

other.sort()


print(other[index - 1])

# 2 3 4
