from re import A
from unicodedata import numeric


frase = input() + "a"
dic = {}
palavra = ""
numero = ""
flag_palavra = 1
for i in frase:
    if(flag_palavra == 1 and i in ["1","2","3","4","5","6","7","8","9","0"]):
        numero += i
        flag_palavra = 0
    elif(flag_palavra == 0 and i in ["1","2","3","4","5","6","7","8","9","0"]):
        numero += i
    if(flag_palavra == 1 and i not in ["1","2","3","4","5","6","7","8","9","0"]):
        palavra += i
    if(flag_palavra == 0 and i not in ["1","2","3","4","5","6","7","8","9","0"]):
        flag_palavra = 1
        dic[int(numero)] = palavra
        palavra = i
        numero = ""

for i in range(1,len(dic.keys())):
    print(dic[i], end=" ")

print(dic[len(dic.keys())])

