def JogoDoToze(n):
    new_n = n

    while new_n > 5:
        new_n -= 3

    if new_n == 4:
        return "vencedor"
    else: 
        return "perdedor"
