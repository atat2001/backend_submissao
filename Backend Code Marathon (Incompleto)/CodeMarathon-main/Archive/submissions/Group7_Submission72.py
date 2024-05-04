def count_duplicates(seq): 
    fir = 0
    sec = 1
    count = 0
    while fir < len(seq):
        while sec < len(seq):
            if seq[fir] == seq[sec]:
                count = count + 1
            sec = sec + 1
        fir = fir + 1
        sec = fir + 1
    return count 

user_input = input()
user_input = "".join(user_input.split(","))
cords = []
icords = [0,0]
input = [user_input[i:i+4] for i in range(0,len(user_input),4)]
for chunk in input:
    counter = 0
    for number in chunk:
        number = int(number)
        if counter == 0:
            for i in range(number):
                icords[1] += 1
                cords += [[icords[0],icords[1]]]
        if counter == 1:
            for i in range(number):
                icords[0] -= 1
                cords += [[icords[0],icords[1]]]
        if counter == 2:
            for i in range(number):
                icords[1] -= 1
                cords += [[icords[0],icords[1]]]
        if counter == 3:
            for i in range(number):
                icords[0] += 1
                cords += [[icords[0],icords[1]]]
        counter += 1
print(count_duplicates(cords))