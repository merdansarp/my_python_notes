# decorators.py
''' DocString'''

from functools import wraps
from time import time

def measure_response_time():
    ''' Measue response time decorator.'''

    def decorator_measure_response_time(func):
        wraps(func)
        def func_measue_respone_time(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            elapsed_time = (end_time - start_time) * 1000

            print(f"Elapsed Time: {elapsed_time} seconds")

            return result
        return func_measue_respone_time
    return decorator_measure_response_time
