# multiple_parameters_two.py

def args_function(*numbers):
    print("*args seems like: ", numbers)
    print("*args type is: ", type(numbers))
    for i in numbers:
        print(i)

def sum_and_print(*numbers):
    result = 0
    print("*args seems like: ", numbers)
    print("*args type is: ", type(numbers))
    enumerated_args = enumerate(numbers, 1)
    for count, item in enumerated_args:
        print(f"{count}. element: {item}")
        result = result + item
    print("Summary of Integers: ", result)

list_of_integers = 6, 7, 8, 9
args_function(list_of_integers)
print("***********************")
sum_and_print(6, 7, 8, 9)
