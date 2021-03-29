import random

class Person():

    def __init__(self, name="Regen KID", age=23, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.location = "Turkey"

    def increase_age(self):
        self.age = self.age + 1
    
    def create_bank_account(self):
        self.account_id = random.randint(10000000, 99999999)
    
    def get_account_id(self):
        return self.account_id

    def move_to_another_country(self, new_country:str):
        self.location = new_country

person_two = Person(name="Debbie Harry", age=75)

print(f"person_two's Name: {person_two.name}, Age: {person_two.age}, Location: {person_two.location}")
person_two.create_bank_account()
print(f"{person_two.name}'s bank acoount id is: {person_two.get_account_id()}")