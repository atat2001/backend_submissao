def Organiza(frase):

    frase_final = []

    for i in frase:
        if i.isnumeric():
            frase_final.append('.')

    palavra = ''

    for char in frase:
        x = char.isalpha()

        if x:
            palavra += char

        else:
            frase_final[int(char) - 1] = palavra
            palavra = ''  

    
    
    return ' '.join(frase_final)

print(Organiza('e2frase4Isto1uma3'))