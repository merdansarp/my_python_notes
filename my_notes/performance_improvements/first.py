# using list comprehensions.

from decorators import measure_response_time

@measure_response_time()
def first_function():
    cube_numbers = []
    for n in range(0,10):
        if n % 2 == 1:
            cube_numbers.append(n**3)

@measure_response_time()
def second_function():
    cube_numbers = [n**3 for n in range(1,10) if n%2 == 1]

def main():
    first_function()
    second_function()

if __name__ == "__main__":
    main()