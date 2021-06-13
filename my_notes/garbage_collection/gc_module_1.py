# gc_module.py

import gc

# check the configured thresholds of your garbage collector
print("Threshoold: ", gc.get_threshold())
# (youngest_generation, next_generation, oldest_generation)
print("Number Of Objects in Generation: ", gc.get_count())
# (youngest_generation, next_generation, oldest_generation)

print(gc.get_count())
print(gc.collect())
print(gc.get_count())
