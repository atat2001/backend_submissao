user_input = input()

arr = []
for n in user_input.split(","):
    arr.append(int(n))

index = arr[0]
other = set()
for i in range(1, 1000):
    other.add(arr[1] * i)
    other.add(arr[2] * i)

other = list(other)
other.sort()

print(other[index - 1])

# 3,2,3
# 2 3 4 6
