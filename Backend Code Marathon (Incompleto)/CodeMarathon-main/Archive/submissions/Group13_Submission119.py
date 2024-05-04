import re
string = str(input())

special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

number = 0
passos = 0

for chr in string:
    if chr.isdigit():
        number=1

capital_letter = any(x.isupper() for x in string)
lower_letter = any(x.islower() for x in string)

if (special_char.search(string) == None):
    flag = 0
else: 
    flag = 1

aux=""
seguidos=1
iguais=0
for chr in string:
    if (aux==chr):
        seguidos+=1
    else:
        aux = chr
        seguidos=1
    if (seguidos>=3):
        iguais+=1

a=0
tamanho = len(string)
if (tamanho>8 and tamanho<=20):
    if (capital_letter==False):
        passos+=1
    if (lower_letter==False):
        passos+=1
    if (number==0):
        passos+=1
    passos+=iguais

elif (tamanho<=8):
    passos = 8 - tamanho + 1
    if (capital_letter==False):
        a+=1
    if (lower_letter==False):
        a+=1
    if (number==0):
        a+=1
    if (passos<a):
        passos=a
    passos+=iguais

elif(tamanho>20):
    passos = tamanho - 20
    if (capital_letter==False):
        passos+=1
    if (lower_letter==False):
        passos+=1
    if (number==0):
        passos+=1
    passos+=iguais

print(passos)
