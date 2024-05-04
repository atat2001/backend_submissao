
stuff = input()


from collections import Counter


ret = Counter(stuff)

print(ret.most_common(1)[0][1])