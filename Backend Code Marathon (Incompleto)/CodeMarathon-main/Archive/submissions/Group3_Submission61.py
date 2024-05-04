user_input = input()

dados = user_input.split("\n")[1:]


minimo = 0
distancia = int(dados[0])
combustivel = int(dados[1])
paragens = []

for p, c in zip(dados[2].split(','), dados[3].split(',')):
    paragens.append((int(p),int(c)))

for p in paragens:
    if combustivel>distancia:
        print(minimo)
        break
    minimo+=1
    combustivel+=p[1]