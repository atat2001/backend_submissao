vec = list(input())

for i in range(0, len(vec)):
    vec[i] = int(vec[i])

start = 0
start_pos = 0
finish = 0
finish_pos = 0
total = 0

greater = 0
greater_pos = -10
second_greater = 0
for i in range(0, len(vec)):
    if vec[i] > greater:
        second_greater = greater
        greater = vec[i]
        greater_pos = i

count = 0
for elem in vec:
    if elem == greater:
        count += 1

if count == 1:
    vec[greater_pos] = second_greater

for i in range(0, len(vec)):
    if vec[i] > start and start == 0 and finish == 0:
        start = vec[i]
        start_pos = i
    
    elif start != 0 and vec[i] >= start:
        finish = vec[i]
        finish_pos = i

    if start != 0 and finish != 0:
        for j in range(start_pos + 1, finish_pos):
            total += (start - vec[j])*100

        start = finish
        start_pos = finish_pos
        finish = 0

print(int(total/100))