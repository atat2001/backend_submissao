class Carro():
    carros = ()
    def __init__(self, matricula: str):
        for i in Carro.carros:
            if matricula in i.Matricula():
                raise ValueError("Carro já criado")
        self._matricula = matricula
        self._EmUso = False
        Carro.carros += (self,)

    @classmethod
    def listacarros(cls):
        return cls.carros

    def Matricula(self):
        return self._matricula

    def EmUso(self):
        return self._EmUso

    def Usar(self):
        self._EmUso = True

    def Tirar(self):
        self._EmUso = False

class ParqueEstacionnamento():
    def __init__(self):
        self._carros = ()
    def listaCarros(self):
        lista = []
        for c in self._carros:
            if c.EmUso():
                lista += [c.Matricula()]
        return lista
    def nCarros(self):
        return len(self.listaCarros())
    def aceitarCarro(self, carro: Carro):
        if self.nCarros() < 5:
            if carro not in self._carros:
                self._carros += (carro,)
            carro.Usar()
    #def rejeitarCarro(self, carro: Carro):
        #count = 0
        #for c in self._carros:
            #if c.EmUso():
                #count += 1
        #if len(self.carros) > 5:

    def alterarEstadoCarro(self, carro):
        carro.Tirar()

n = input()
Parque = ParqueEstacionnamento()
for i in range(int(n)):
    str = input()
    l = str.split(" - ")
    if l[0] == "aceitarCarro":
        try:
            Parque.aceitarCarro(Carro(l[1]))
        except ValueError:
            for i in Carro.listacarros:
                if i.Matricula() == l[1]:
                    Parque.aceitarCarro(i)
    if l[0] == "sairCarro":
        for i in Carro.listacarros:
            if i.Matricula() == l[1]:
                Parque.alterarEstadoCarro(i)
print(Parque.nCarros())
for i in Parque.listaCarros():
    print(i)


            




'''c1 = Carro("44-YH-66")
c2 = Carro("44-YH-67")
c3 = Carro("44-YH-68")
c4 = Carro("44-YH-69")
c5 = Carro("44-YH-70")
c6 = Carro("44-YH-81")
Parque = ParqueEstacionnamento()
Parque.aceitarCarro(c1)
Parque.aceitarCarro(c2)
Parque.aceitarCarro(c3)
Parque.aceitarCarro(c4)
Parque.aceitarCarro(c5)
Parque.aceitarCarro(c6)
Parque.aceitarCarro(c1)
Parque.alterarEstadoCarro(c1)
Parque.aceitarCarro(c6)
Parque.alterarEstadoCarro(c2)
Parque.aceitarCarro(c1)

print(Parque.nCarros())
for i in Parque.listaCarros():
    print(i)'''

