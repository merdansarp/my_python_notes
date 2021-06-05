# unpacking.py

new_array = [6, 7, 8, 9, 10, 11]
print("Our List: ", new_array, "\n")
print("Unpack our list with * -> Asterisk")
print(*new_array, "\n")

a, *b, c = new_array
print(f"Unpack {new_array} with multiple *args")
print(a, b, c)