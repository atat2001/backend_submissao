#!/bin/python3


class Carro:

    def __init__(self, matricula: str, em_uso: bool):
        self.matricula = matricula
        self.em_uso = em_uso


class ParqueEstacionamento:

    def __init__(self):
        self.carros: dict[str, Carro] = {}

    def aceitarCarro(self, matricula: str):
        if matricula in self.carros:
            self.alterarEstadoCarro(matricula, True)

        self.carros[matricula] = Carro(matricula, True)

    def sairCarro(self, matricula: str):
        if matricula in self.carros:
            self.alterarEstadoCarro(matricula, False)

    def rejeitarCarro(self, matricula: str):
        del self.carros[matricula]

    def alterarEstadoCarro(self, matricula: str, em_uso: bool):
        self.carros[matricula].em_uso = em_uso

    def print(self):
        total = 0
        for matricula, carro in self.carros.items():
            if carro.em_uso:
                total += 1

        print(total)
        for matricula, carro in self.carros.items():
            if carro.em_uso:
                print(matricula)


if __name__ == '__main__':
    parque = ParqueEstacionamento()

    instructions = int(input())
    for _ in range(instructions):
        metodo, matricula = input().split(" - ")
        print(metodo, matricula)
        if metodo == 'aceitarCarro':
            parque.aceitarCarro(matricula)
        elif metodo == 'sairCarro':
            parque.sairCarro(matricula)
        else:
            assert False
    parque.print()
