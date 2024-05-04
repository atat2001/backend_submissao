user_input = input()

carros = []
for l in user_input.split("\n")[1:]:
    if "aceitarCarro" in l:
        carros.append(l.split(" ")[-1])
    if "sairCarro" in l:
        carros.remove(l.split(" ")[-1])

carros = list(dict.fromkeys(carros))

s = ""
s+=str(len(carros))+"\n"
for c in carros:
    s+=c
    if c!=carros[-1]:
        s+="\n"

output = s
print(output)