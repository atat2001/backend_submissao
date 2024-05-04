user_input = input()
user_input = int(user_input)
if user_input - 1 % 4 == 0:
    print("perdedor")
else:
    print("vencedor")