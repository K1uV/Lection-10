age_factor = 7
class Dog(age_factor = 7):
    def __init__(self, age):
        self.age = age

    def human_age(self):
        a = self.age * 7
        print(a)

my_dog = Dog('23')
my_dog.human_age()  