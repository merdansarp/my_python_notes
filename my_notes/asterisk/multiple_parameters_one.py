# multiple_parameters_one.py

def sum_and_print(integers_list):
    result = 0
    for i in range(len(integers_list)):
        print(f"{i+1}. element:" , integers_list[i])
        result = result + integers_list[i]
    
    print(f"Sumamry of Integer List: ", result)
    return result

def sum_and_print_two(first_number, second_number):
    result = 0
    print(f"Numbers are {first_number} and {second_number}")
    result = first_number + second_number
    print(f"Summary of Two Numbers: ", result)
    return result

list_of_integers = [6, 7, 8, 9]
sum_and_print(list_of_integers)
print("***********************")
a, b = 14, 15
sum_and_print_two(a, b)
