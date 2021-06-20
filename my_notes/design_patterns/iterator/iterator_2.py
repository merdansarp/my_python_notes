# iterator py file
""" Create an iterator. """

class MyNumbersByTwo:
    """ Iterator Class. To use it add __iter__ and __next__ medthods. """
    def __iter__(self):
        """ Iter class. """
        self.first_param = 1
        return self
    
    def __next__(self):
        """ Next Class. """
        if self.first_param < 16:
            next_param = self.first_param
            self.first_param += 2
            return next_param
        else:
            raise StopIteration

myclass = MyNumbersByTwo()
myiters = iter(myclass)

print(next(myiters))
print(next(myiters))
print(next(myiters))

for i in myiters:
    print(f"For Loop: {i}")
