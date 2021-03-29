class Person():

    def __init__(self, name="Regen KID", age=23, sex=None):
        self.name = name
        self.age = age
        self.sex = sex


person_one = Person()
person_two = Person(name="Debbie Harry", age=75, sex="Female")

print(f"person_one's Name: {person_one.name}, Age: {person_one.age}, Sex: {person_one.sex}")
print(f"person_two's Name: {person_two.name}, Age: {person_two.age}, Sex: {person_two.sex}")