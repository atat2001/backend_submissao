import re

user_input = input()
match = re.findall(r"([a-z]+)([0-9]+)", user_input, re.I)

d = dict((y, x) for x, y in match)

result = ""
for key in sorted(d):
    result += d[key] + " "

print(result)
