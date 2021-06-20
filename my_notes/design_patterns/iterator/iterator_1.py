# iterator py file
""" Iterator Example"""

our_project_tuple = ("notifier", "asgard", "edith", "watch_cat", "code_hunter")
my_iterations = iter(our_project_tuple)

print(next(my_iterations))
print(next(my_iterations))

ex_string = "CafeXOR"
for i in ex_string:
    print(i)
