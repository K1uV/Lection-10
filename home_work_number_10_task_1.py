class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print("Здравствуйте, меня зовут" + '' + self.name.title() + '' +  self.surname.title() +'' +  'и мне' + '' +'' self.age +''+ ' лет')

my_person = Person('Antony', 'Johnson', '35')
my_person.talk()