def leet():
    user_input = input()

    if not user_input:
        return 0

    user_input = int(user_input)

    count = 0
    for i in range(user_input):
        s = str(i)

        for j in s:
            if j == "0" or j == "1":
                count += 1

    print(count)


if __name__ == "__main__":
    leet()
