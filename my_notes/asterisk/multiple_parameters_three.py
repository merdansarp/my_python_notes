# multiple_parameters_three.py

def sum_and_print(**numbers):
    print("**kwargs seems like: ", numbers)
    print("**kwargs type is: ", type(numbers))
    result = 0
    for key in numbers:
        print(f"{key}:{numbers[key]}")
        result = result + numbers[key]
    print("Sumamry of Numbers: ", result)
    return result

sum_and_print(a=6, b=7, c=8, d= 9)
# first_dict = {
#     "a": 2,
#     "b": 3,
#     "c": 4
# }

# second_dict = {
#     "c": 6,
#     "d": 41,
#     "e": 19
# }
# sum_and_print(first_dict, second_dict)