word1, word2 = input().split(",")
word1 = list(word1)
word2 = list(word2)

def frenetic3():
    global word1, word2

    prev_letter = ""
    to_delete = []
    for i in range(0, len(word2)):
        if word2[i] == prev_letter:
            to_delete.append(i-len(to_delete))

        prev_letter = word2[i]

    for i in to_delete:
        del word2[i]

    if word1 == word2:
        print("true")
    else:
        print("false")

frenetic3()