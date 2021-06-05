class Person():

    def __init__(self, name, age=27, location="Turkey"):

        self.__name = name
        self.__age = age
        self.__location = location
    
    def __print_person_details(self):
        """ Private Method. We can use this method only in this class. """

        print(f"Person Details: {self.__name} {self.__age} {self.__location}")

    def access_from_outside(self):
        """ 
        We cannot access to public method in any shape or form. So We use the public method to 
        access private/protected methods/variables.
        We can use private method here because we are in it's class scope.
        """
        self.__print_person_details()


person_one = Person("Debbie Harry", 75, "USA")
person_one.access_from_outside()
person_one.__print_person_details()