radio = int(input())

total = 0

total += radio // 11
radio = radio % 11

total += radio // 3
radio = radio % 3

total += radio // 1
radio = radio % 1

print(total)
