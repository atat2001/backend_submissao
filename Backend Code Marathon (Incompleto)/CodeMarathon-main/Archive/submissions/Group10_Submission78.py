def JogoDoToze(n):
    if (n - 1) % 4 == 0:
        return 'perdedor'
    else:
        return 'vencedor'
    

print(JogoDoToze(7))

