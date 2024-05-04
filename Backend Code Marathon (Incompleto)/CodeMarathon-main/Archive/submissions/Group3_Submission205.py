user_input = input()

letters = set(user_input)
max_count = 0
freq_letter = []
for letter in letters:
    count = 0
    for char in user_input:
        if char == letter:
            count += 1
    if count == max_count:
        max_count = count
        freq_letter.append(letter)
    if count > max_count:
        max_count = count
        freq_letter.clear()
        freq_letter.append(letter)
print(int(freq_letter[0]))