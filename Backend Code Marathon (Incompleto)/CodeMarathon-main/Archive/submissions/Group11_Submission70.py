class Carro:
    def __init__(self, matricula, EmUso):
        self.matricula = matricula
        self.EmUso = True

class ParqueEstacionamento:
    def __init__(self):
        self.carros = {True: [], False: []}
        self.limite = 5

    def aceitarCarro(self, carro):
        carro = Carro(carro, False)
        self.carros[False].append(carro)
        
    def rejeitarCarro(self, carro):
        if len(self.carros[False]) < 5 and carro not in self.carros[False]:
            self.aceitarCarro(carro)

    def alterarEstadoCarro(self, carro):
        if carro in self.carros[False]:
            self.carros[True] = carro
            self.carros[False].remove(carro)
        else:
            self.carros[False] = carro
            self.carros[True].remove(carro)

parque = ParqueEstacionamento()
num_inputs = int(input())
output = ""

while num_inputs > 0:
    current_input = input()
    current_input = current_input.split(" ")
    current_input.remove("-")
    carro = current_input[-1]
    if current_input[0] == "aceitarCarro":
        parque.rejeitarCarro(carro)
    else:
        parque.alterarEstadoCarro(carro)
    num_inputs -= 1

output += len(parque.carros[True]) + "\n"

for carro in parque.carros[True]:
    output += carro + "\n"

print(output)