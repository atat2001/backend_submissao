class Carro:
    def __init__(self, matricula, EmUso, admission_num):
        self.matricula = matricula
        self.EmUso = EmUso
        self.admission_num = admission_num

class ParqueEstacionamento:
    def __init__(self):
        self.carros = {True: [], False: []}
        self.limite = 5
        self.counter = -1

    def aceitarCarro(self, carro):
        self.counter += 1
        carro = Carro(carro, False, self.counter)
        self.carros[False].append(carro)
        
    def rejeitarCarro(self, carro):
        bool = False

        for car in self.carros[False]:
            if car.matricula == carro: bool = True

        if len(self.carros[False]) < 5 and not bool:
            self.aceitarCarro(carro)

    def alterarEstadoCarro(self, carro):
        car = None

        for current_car in self.carros[False]:
            if current_car.matricula == carro: car = current_car 

        for current_car in self.carros[True]:
            if current_car.matricula == carro: car = current_car

        if car in self.carros[False]:
            self.carros[True].append(car)
            if car in self.carros[False]: self.carros[False].remove(car)
        else:
            self.carros[False].append(car)
            if car in self.carros[True]: self.carros[True].remove(car)

parque = ParqueEstacionamento()
num_inputs = int(input())
output = ""

while num_inputs > 0:
    current_input = input()
    current_input = current_input.split(" ")
    carro = current_input[-1]
    if current_input[0] == "aceitarCarro":
        parque.rejeitarCarro(carro)
    else:
        parque.alterarEstadoCarro(carro)
    num_inputs -= 1

output += str(len(parque.carros[False])) + "\n"

parque.carros[False].sort(key = lambda x: x.admission_num, reverse=True)

for carro in parque.carros[False]:
    output += carro.matricula + "\n"

print(output)