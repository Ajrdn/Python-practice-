numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:3])
print(numbers[:2])
print(numbers[2:])
print(numbers[:])

print(numbers[0:6:2])
print(numbers[1:6:2])
print(numbers[6:0:-1])

del numbers[0:2]
print(numbers)

numbers[1:3] = [6, 8]
print(numbers)

numbers[0:2] = [9, 10, 11]
print(numbers)

numbers[1:3] = [1]
print(numbers)
