# one line assignments.

from decorators import measure_response_time

@measure_response_time()
def first_function():
    a, b, c, d = "Red", "Hot", "Chili", "Peppers"
    return a, b, c, d

@measure_response_time()
def second_function():
    a = "Red"
    b = "Hot"
    c = "Chili"
    d = "Peppers"
    return a, b, c, d

def main():
    first_function()
    second_function()

if __name__ == "__main__":
    main()