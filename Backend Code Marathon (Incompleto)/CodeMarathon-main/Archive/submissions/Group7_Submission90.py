user_input = input().split(',')

word=[]
for char in user_input[0]:
    if char.isalpha(): word.append(char)
    else: word=word*int(char)

print(word[int(user_input[1])-1])




