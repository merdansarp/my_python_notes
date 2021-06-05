from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def calculate_happiness():
        pass


class Developer(Person):

    def __init__(self, name: str, age: int, company: str, location: str):
        super().__init__(name, age)
        self.company = company
        self.location = location

    def get_real_age(self):
        return self.age * 1.5
    
    def calculate_happiness(self):
        country_happiness = {
            "USA": 10,
            "Turkey": 9,
            "UK": 11,
            "Canada": 12,
        }
        hapiness = country_happiness[self.location] / self.age
        return hapiness

developer_1 = Developer("Dennis Ritchie", 70, "Lucent Technologies", "USA")
print(developer_1.calculate_happiness())
person_1 = Person("John Doe", 123)
person_1.calculate_happiness()