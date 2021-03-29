class Person():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_real_age(self):
        return self.age


class Musician(Person):

    def __init__(self, name: str, age: int, genre: str, band: str, instrument=None):
        super().__init__(name, age)
        self.genre = genre
        self.band = band
        self.insturment = instrument


person_1 = Person("John Doe", 33)
print(f"person_1's age: {person_1.age} and real age: {person_1.get_real_age()}")
musician_1 = Musician("Debbie Harry", 75, "New Vave/Punk", "Blondie")
print(f"musician_1's age: {musician_1.age} and real age: {musician_1.get_real_age()}")


class Developer(Person):

    def __init__(self, name: str, age: int, company: str, location: str):
        super().__init__(name, age)
        self.company = company
        self.location = location

    def get_real_age(self):
        return self.age * 1.5


developer_1 = Developer("Dennis Ritchie", 70, "Lucent Technologies", "USA")
developer_1.get_real_age()
print(f"developer_1's age: {developer_1.age} and real age: {developer_1.get_real_age()}")