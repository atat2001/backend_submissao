def Vindimas(n):
    primeiro = 0
    segundo = 0
    terceiro = 0

    barreira_2 = 0
    barreira_1 = 0
    barreira_menor = 0

    soma_aux = 0
    index_aux = 0

    soma = 0

    pode_ter_barreira = False

    for numero in n:
        numero = int(numero)

        soma_aux += numero
        index_aux += 1

        primeiro = segundo
        segundo = terceiro
        terceiro = numero

        if numero != 0:
            pode_ter_barreira = True
        
        if segundo > primeiro and segundo > terceiro and pode_ter_barreira:
            barreira_1 = barreira_2
            barreira_2 = segundo

            if barreira_1 <= barreira_2:
                barreira_menor = barreira_1

            else:
                barreira_menor = barreira_2

            soma += index_aux * barreira_menor - soma_aux

            index_aux = 0

            soma_aux = 0

        print(soma, soma_aux)

    return soma


print(Vindimas('010210132121'))