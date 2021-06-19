""" Context Manager Example"""

with open('red_hot_chili_peppers.txt', 'r') as opened_file:
    data = opened_file.read()

splitted_data = data.split()
print(splitted_data[0], splitted_data[1])


# Write with 'with'
with open('new_file.txt', 'w') as opened_file:
    opened_file.write("This is a new file! ")

# Same as Write with 'with'
file = open('new_file.txt', 'w')
try:
    file.write("Different Write Method")
finally:
    file.close()

