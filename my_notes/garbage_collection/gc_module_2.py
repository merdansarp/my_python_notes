# gc_module_2.py

import gc

# In the example above, we increase each of our thresholds from their defaults. 
# Increasing the threshold will reduce the frequency at which the garbage collector runs. 
# This will be less computationally expensive in your program at the expense of keeping dead objects around longer.
print("Threshoold: ", gc.get_threshold())
# (youngest_generation, next_generation, oldest_generation)
gc.set_threshold(1000, 20, 30)
print("Threshoold: ", gc.get_threshold())
