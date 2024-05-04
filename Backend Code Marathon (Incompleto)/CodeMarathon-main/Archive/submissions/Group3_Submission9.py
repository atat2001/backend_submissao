user_input = input()

alturas = []

for s in user_input:
    alturas.append(int(s))

total = 0
maior = 0

for i, h in enumerate(alturas):
    for h2 in alturas[i+1:]:
        if h2>h:
            total+=max((maior-h),0)
            break
    else:
        maior = h
        continue
    if h>maior:
        maior = h
    

output = total
print(output)