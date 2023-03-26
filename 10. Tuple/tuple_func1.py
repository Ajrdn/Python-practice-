list = [1, 2, 3, 4, 5]

for tuple in enumerate(list):
    print(f'{tuple[0]}번째 값: {tuple[1]}')

for tuple in enumerate(list):
    print('{}번째 값: {}'.format(*tuple))
