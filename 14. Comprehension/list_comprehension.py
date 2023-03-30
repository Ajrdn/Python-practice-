list1 = [i * i for i in range(1, 11)]

print(list1)

list2 = [i * i for i in range(1, 11) if i % 2 == 0]

print(list2)

list3 = [(x, y) for x in range(15) for y in range(15)]

print(list3)
