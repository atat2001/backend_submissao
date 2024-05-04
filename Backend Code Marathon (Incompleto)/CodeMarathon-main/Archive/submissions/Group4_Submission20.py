class Carro:
    def __init__(self,matricula,emUso) -> None:
        self.matricula = matricula
        self.emUso = emUso

class ParqueEstacionamento:


    def __init__(self,limite=5) -> None:
        self.carros = []
        self.limite = limite

    def aceitarCarro(self,matricula):
        emUso = False
        if self.limite > 0:
            self.limite -=1
            emUso = True
        carro = Carro(matricula,emUso)
        self.carros.append(carro)
        
           


    def rejeitarCarro(self):
        return

    def alterarEstadoCarro(self,aEntrar,matricula):

        if aEntrar:
            if self.limite == 0:
                return
            for carro in self.carros:
                if carro.matricula == matricula:
                    carro.emUso = True
                    return
            carro = Carro(matricula,True)
            self.carros.append(carro)
            self.limite -=1
        else:
            for carro in self.carros:
                if carro.matricula == matricula:
                    carro.emUso = False
                    self.limite +=1
                    return



num_instrucoes = int(input(''))
parque = ParqueEstacionamento()
while num_instrucoes != 0:
    instrucao = str(input(''))
    func,matricula = instrucao.split(' - ')
    if func == "aceitarCarro":
        parque.aceitarCarro(matricula)
    elif func == "sairCarro" :
        parque.alterarEstadoCarro(False,matricula)

    num_instrucoes-=1

print(len(parque.carros))

for carro in parque.carros:
    if carro.emUso:
        print(carro.matricula)