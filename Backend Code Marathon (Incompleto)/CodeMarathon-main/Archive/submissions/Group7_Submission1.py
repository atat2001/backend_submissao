user_input = input()
tinput=[]
for i in range(int(user_input)):
    a = input()
    tinput.append(a)

cars = []
for car in tinput:
    c = car.split(' - ')
    if c[0]=='aceitarCarro': cars.append(c[-1]) if c[-1] not in cars else None
    else: cars.remove(c[-1])

print(len(cars))
for car in cars:
    print(car)