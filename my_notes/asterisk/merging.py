# merging.py

first_list = [5, 6, 7]
second_list = [5, 66, 77]
print(f"Two lists: {first_list} and {second_list}")
merged_list = [*first_list, *second_list]
print(f"Merged List with Asterisk: {merged_list} \n\n")

first_dict = {
    "a": 2,
    "b": 3,
    "c": 4
}

second_dict = {
    "c": 6,
    "d": 41,
    "e": 19
}

print(f"Two dicts: {first_dict} and {second_dict}")
merged_dict = {**first_dict, **second_dict}
print(f"Merged Dict With Asterisk: {merged_dict} \n\n")
