dict = {
    '하나': 1,
    '둘': 2,
    '셋': 3,
}

for tuple in dict.items():
    print(f'{tuple[0]}: {tuple[1]}')

for tuple in dict.items():
    print('{}: {}'.format(*tuple))
