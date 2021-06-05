class Person():

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


first_person = Person("Selami", 77, "Male")

print(first_person.name)
print(first_person.age)
print(first_person.sex)