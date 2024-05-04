initial = input()

initial_chart = [int(letter) for letter in str(initial)]

charts = [[] for _ in range(max(initial_chart))]

for i in range(len(charts)):
    for j in range(len(initial_chart)):
        if initial_chart[j] > i:
            charts[i].append(1)
        else:
            charts[i].append(0)

charts.reverse()

sum = 0

for chart in charts:
    a = ''.join([str(i) for i in chart])
    a = int(a)
    while a % 10 == 0:
        a //= 10
    a = str(a)
    a = a.replace('1', '')
    sum += len(a)

print(sum)
    