class Person():

    def __init__(self, name, age=23, sex=None):
        self.__name = name
        self.age = age
        self.sex = sex
    
    def get_name(self):
        return self.__name


person_two = Person(name="Debbie Harry", age=75, sex="Female")
print(f"person_two's Name: {person_two.name()}, Age: {person_two.age}, Sex: {person_two.sex}")
print(f"person_two's Name: {person_two.get_name()}, Age: {person_two.age}, Sex: {person_two.sex}")
