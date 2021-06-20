# generator functions
""" Generator examples. """

def generator():
    print("First Step!")
    yield(1)

    print("Second Step!")
    yield(2)

    print("Dev'sTEP!!")
    yield(3)

def main():
    my_gen = generator()
    next(my_gen)
    print("After first")
    next(my_gen)
    print("After Second")
    next(my_gen)

if __name__ == "__main__":
    main()
