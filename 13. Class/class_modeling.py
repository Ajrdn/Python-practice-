class Human:
    '''사람'''

def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

def eat(person):
    person.weight += 0.1
    print(f'{person.name}가 먹어서 {person.weight}KG이 되었습니다.')

def walk(person):
    person.weight -= 0.1
    print(f'{person.name}가 걸어서 {person.weight}KG이 되었습니다.')

Human.create = create_human
Human.eat = eat
Human.walk = walk

person = Human.create('철수', 60.5)
person.walk()
person.eat()
person.walk()
