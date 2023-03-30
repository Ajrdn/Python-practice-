class Human:
    '''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = '한국인'
person2.name = '미국인'

def speak(person):
    print(f'{person.name}이 {person.language}로 말을 합니다.')

Human.speak = speak

person1.speak()
person2.speak()
