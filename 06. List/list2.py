list = [37, 23, 10, 33, 29, 40]
print(list)

list.append(16)
print(list)

list += [19]
print(list)

n = 33
print(n in list)

del list[2]
del(list[2])
print(list)

list.remove(40)
print(list)
