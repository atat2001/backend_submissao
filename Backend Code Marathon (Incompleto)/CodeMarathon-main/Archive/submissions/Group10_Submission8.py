def JogoDoToze(n):
    n = int(input())

    if (n -1) % 4 == 0:
        return "perdedor"
    else: 
        return "vencedor"
