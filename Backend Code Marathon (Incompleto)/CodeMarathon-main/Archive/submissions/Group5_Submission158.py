inp = str(input())
inp = inp.split(",")

nrAlunos = len(inp)
classifcs = [int(inp[i]) for i in range(nrAlunos)]
notas = [1 for _ in range(nrAlunos)]

for cl in range(2, 10):
    for i in range(nrAlunos):
        if cl != classifcs[i]:
            continue
        
        if i == 0: # Ponta esquerda
            if classifcs[i] > classifcs[i+1]:
                notas[i] = notas[i+1] + 1
                
        elif i == nrAlunos - 1: # Ponta Direita
            if classifcs[i] > classifcs[i-1]:
                notas[i] = notas[i-1] + 1
                
        else: # Caso geral
            maiorNota = notas[i]
            if classifcs[i] > classifcs[i-1]:
                maiorNota = max(maiorNota, notas[i-1] + 1)
            if classifcs[i] > classifcs[i+1]:
                maiorNota = max(maiorNota, notas[i+1] + 1)
            
            notas[i] = maiorNota
            
print(sum(notas))