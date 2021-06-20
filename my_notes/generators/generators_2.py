# generator functions
""" Generator with loops examples. """

def generator_square(number):
    for i in range(1, number):
        yield i * i

def main():
    my_gen = generator_square(5)
    try:
        print(next(my_gen))
        print(next(my_gen))
        print(next(my_gen))
        print(next(my_gen))
        print(next(my_gen))
    except StopIteration:
        print("Iteration has stopped.")

if __name__ == "__main__":
    main()
