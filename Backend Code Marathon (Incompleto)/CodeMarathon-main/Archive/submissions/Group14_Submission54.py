#!/bin/python3


class Carro:

    def __init__(self, matricula: str, em_uso: bool):
        self.matricula = matricula
        self.em_uso = em_uso


class ParqueEstacionamento:

    def __init__(self):
        self.carros: dict[str, Carro] = {}
        self.maximo: int = 5
        self.ocupados: int = 0

    def aceitarCarro(self, matricula: str):
        if self.maximo <= self.ocupados:
            return

        if matricula in self.carros:
            if self.carros[matricula].em_uso == False:
                self.alterarEstadoCarro(matricula, True)
                self.ocupados += 1
        else:
            self.carros[matricula] = Carro(matricula, True)
            self.ocupados += 1

    def sairCarro(self, matricula: str):
        if matricula in self.carros:
            self.alterarEstadoCarro(matricula, False)
            self.ocupados -= 1

    def rejeitarCarro(self, matricula: str):
        pass

    def alterarEstadoCarro(self, matricula: str, em_uso: bool):
        self.carros[matricula].em_uso = em_uso

    def print(self):
        print(self.ocupados)
        for matricula, carro in self.carros.items():
            if carro.em_uso:
                print(matricula)


if __name__ == '__main__':
    parque = ParqueEstacionamento()

    instructions = int(input())
    for _ in range(instructions):
        metodo, matricula = input().split(" - ")
        # print(metodo, matricula)
        if metodo == 'aceitarCarro':
            parque.aceitarCarro(matricula)
        elif metodo == 'sairCarro':
            parque.sairCarro(matricula)
        else:
            assert False
    parque.print()
