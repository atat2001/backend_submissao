user_input = input()

letters,words,indexs = [],[],[]
for char in user_input:
    if char.isalpha(): letters.append(char)
    else: 
        indexs.append(char)
        words.append(''.join(letters))
        letters=[]

nwords = words.copy()
for i in range(len(indexs)):
    nwords[int(indexs[i])-1]=words[i]

print(' '.join(nwords))
