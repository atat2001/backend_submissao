ana, scooby, atual = input().split(',')

def dias(data):
    sum = 0
    sum += int(data[0:2])
    sum += int(data[2:4]) * 30
    sum += int(data[4:]) * 365
    return sum

ana = dias(ana)
scooby = dias(scooby)
atual = dias(atual)

print((atual - ana) > ((atual - scooby) * 7))