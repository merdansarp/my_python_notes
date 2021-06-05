class Person:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
        # with adding underscope to salary on the left side, we can observe class behaviour (self._salary)

    @property
    def salary(self):
        print("Get Salary Method Running ... ")
        return self._salary

    @salary.setter
    def salary(self, value):
        print("Set Salary Method Running ... ")
        if value > 15000:
            print("You're RICH! You should pay taxes")
            self._salary = (value * 0.6) 
        else:
            print("You're POOR! You should pay more taxes")
        self._salary = (value * 0.4)


person_one = Person("Debbie Harry", 6666)
print(f"{person_one.name}'s real salary is: {person_one.salary}")
person_one.salary = 4584000
print(f"{person_one.name}'s real salary is: {person_one.salary}")