class Person():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age = self.age + 1

    def decrease_age(self):
        self.age = self.age - 1

    def get_name(self):
        print("Getting Person Name ....")
        print(self.name)


class Developer():

    def __init__(self, name:str, nickname:"NEO", company=None, location="Turkey"):
        self.name = name
        self.nickname = nickname
        self.company = company
        self.location = location

    def move_to_another_country(self, new_location):
        self.location = new_location

    def change_nickname(self, new_nickname):
        print("You cannot change your nickname")

    def get_name(self):
        print("Developer Name")
        return self.name


class DevPerson(Person, Developer):

    def __init__(self, name, age, nickname, company, location):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.company = company
        self.location = location

    def change_nickname(self, new_nickname):
        """ Overriding :D """
        self.nickname = new_nickname

person_1 = Person("Ada Lovelace", 206)
developer_1 = Developer("John Anderson", "Neo", "SomeWhereCoop", "USA")
person_1.increase_age()
person_1.decrease_age()
developer_1.change_nickname("NeoOfZion")
print(f"Person ONE: {person_1.name}, {person_1.age}")
print(f"Developer ONE: {developer_1.name}, {developer_1.nickname}, {developer_1.company}, {developer_1.location}")

hybrid_1 = DevPerson("Fiona Apple", 45, "Fiona", "SomeWhereCoop", "USA")
print(f"Hybrid ONE: {hybrid_1.name}, {hybrid_1.age}, {hybrid_1.nickname}, {hybrid_1.company}, {hybrid_1.location}")
hybrid_1.get_name()
# We get the Person Class's get_name function because while we define hybrid class, we defined Person before Developer.
hybrid_1.increase_age()
hybrid_1.change_nickname("Hot Knife")
hybrid_1.increase_age()
hybrid_1.move_to_another_country("Turkey")
hybrid_1.decrease_age()
print(f"Hybrid ONE: {hybrid_1.name}, {hybrid_1.age}, {hybrid_1.nickname}, {hybrid_1.company}, {hybrid_1.location}")