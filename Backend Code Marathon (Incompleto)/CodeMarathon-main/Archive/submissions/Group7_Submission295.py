user_input = input()
x = user_input.split(",")
data = [int(num) for num in x]
if data[0] // 10000 < data[2] // 1000:
    anos_ana = (data[3] % 10000) - (data[0] % 10000) - 1
elif data[0] // 10000 > data[2] // 1000:
    anos_ana = (data[3] % 10000) - (data[0] % 10000)
if data[1] // 10000 < data[2] // 1000:
    anos_cao = 7 * ((data[3] % 10000) - (data[0] % 10000) - 1)
elif data[1] // 10000 > data[2] // 1000:
    anos_cao = 7 * ((data[3] % 10000) - (data[0] % 10000))
print(anos_ana > anos_cao)





