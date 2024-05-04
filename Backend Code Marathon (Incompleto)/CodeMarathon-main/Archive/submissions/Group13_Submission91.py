from audioop import mul
from turtle import position


x = input()

y = x.split(",")

num_it = int(y[0])


n1 = int(y[1])
n2 = int(y[2])

multiplos = []

for i in range(1, num_it + 1):
    multiplos.append(n1*i)
    multiplos.append(n2*i)

multiplos.sort()
print(multiplos[num_it-1])

