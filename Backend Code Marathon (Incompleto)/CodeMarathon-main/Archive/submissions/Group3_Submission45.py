user_input = int(input())

n_galhos = user_input
""" galhos_meus = 0 
galhos_toze = 0 """
if n_galhos % 4 == 0:
    output = "vencedor"
else:
    output = "perdedor"


print(output)