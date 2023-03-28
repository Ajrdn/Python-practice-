class Human:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}(몸무게 {self.weight}KG)'

    def eat(self):
        self.weight += 0.1
        print(f'{self.name}가 먹어서 {self.weight}KG이 되었습니다.')

    def walk(self):
        self.weight -= 0.1
        print(f'{self.name}가 걸어서 {self.weight}KG이 되었습니다.')

    def speak(self, message):
        print(message)

person = Human('사람', 60.5)
print(person)
