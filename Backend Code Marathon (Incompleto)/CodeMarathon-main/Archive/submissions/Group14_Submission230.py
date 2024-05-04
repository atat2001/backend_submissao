scrambled = input()
word = ''

sentence = []


def is_digit(char):
    return char >= '0' and char <= '9'


for char in scrambled:
    if is_digit(char):
        sentence.append((int(char), word))
        word = ''
        continue

    word += char

for index, word in sorted(sentence):
    print(word, end=' ')
print()
