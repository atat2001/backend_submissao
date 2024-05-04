user_input = input()


def andar(i):
    if i == len(user_input)-1:
        print("true")
        exit()
    if user_input[i] == "0":
        return
    andar(i+int(user_input[i]))
    if i-int(user_input[i])>0:
        andar(i-int(user_input[i]))
    return

andar(0)
print("false")