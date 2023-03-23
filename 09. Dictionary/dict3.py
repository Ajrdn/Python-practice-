dict = {
    'one': 1,
    'two': 2,
}
print(dict)

dict['one'] = 11
print(dict)

dict['three'] = 3
print(dict)

del(dict['one'])
print(dict)

print(dict.pop('two'))
print(dict)
