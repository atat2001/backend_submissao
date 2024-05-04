from posixpath import split


class Carro:
    def __init__(self, matricula):
        self.matricula = matricula
        self.emUso = False
    
    def setEmUso(self):
        self.emUso = True
    
    def getIsEmUso(self):
        return self.emUso
    
    def getMatricula(self):
        return self.matricula

class ParqueEstacionamento:
    def __init__(self):
        self.carrosDentro = []
        self.limite = 5
        self.carrosTotal = {}
    
    def getLugaresEmUso(self):
        return len(self.carrosDentro)
    
    def receberCarro(self, matricula):
        if matricula not in self.carrosTotal.keys():
            carro = Carro(matricula)
        else:
            carro = self.carrosTotal[matricula]
            
        if self.limite > len(self.carrosDentro) and matricula not in self.carrosDentro:
            self.carrosDentro.append(matricula)
            carro.emUso = True
        self.carrosTotal[matricula] = carro
    
    def retirarCarro(self,matricula):
        if matricula in self.carrosDentro:
            self.carrosDentro.remove(matricula)
            self.carrosTotal[matricula].emUso = False
     
 
if __name__ == '__main__':
    parque = ParqueEstacionamento() 
    lines = int(input(""))
    for _ in range(lines):
        line = input("").split(" - ")
        if line[0] == "aceitarCarro":
            parque.receberCarro(line[1])
        elif line[0] == "sairCarro":
            parque.retirarCarro(line[1])
    print(parque.getLugaresEmUso())
    for carro in sorted(parque.carrosDentro):
        print(carro)
        