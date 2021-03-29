class Person():

    def __init__(self, name, age=23, sex=None):
        self.__name = name
        self.age = age
        self.sex = sex
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


person_two = Person(name="Debbie Harry", age=75, sex="Female")
print(f"person_two's Name: {person_two.get_name()}, Age: {person_two.age}, Sex: {person_two.sex}")
person_two.set_name("New Debbie")
print(f"person_two's Name: {person_two.get_name()}")
