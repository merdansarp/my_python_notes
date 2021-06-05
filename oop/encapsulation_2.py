class Person():

    _name = None
    _age = None
    _location = None

    def __init__(self, name, age=27, location="Turkey"):
        """ This is constructor method. """
        self._name = name
        self._age = age
        self._location = location
    
    def _show_ages_and_locations(self):
        """ Protected Function. We Can access to protected data members"""

        print("Age: ", self._age)
        print("Location: ", self._location)

class Developer(Person):

    def __init__(self, name, age, location, company):
        super().__init__(name, age, location)
        self.company = company

    def show_developer_info(self):
        """ We create public method and we can access to protected data 
        members and methods of super class in here. """

        print("Developer's Name: ", self._name)
        self._show_ages_and_locations()


dev_one = Developer("Dennis Ritchie", 70, "USA", "Lucent Technologies")
dev_one.show_developer_info()