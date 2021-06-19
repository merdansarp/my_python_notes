# decorators.py
''' DocString'''

from functools import wraps
from time import time

def exception_handler():
    ''' Exception Handler Decorator. If any exception occurs, don't stop just print exception. '''

    def decorator_exception_handler(func):
        @wraps(func)
        def func_exception_handler(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except Exception as exception: # pylint: disable=broad-except
                print("Exception Occured! -> ", str(exception))
        
        return func_exception_handler
    return decorator_exception_handler

def measure_response_time():
    ''' Measue response time decorator.'''

    def decorator_measure_response_time(func):
        wraps(func)
        def func_measue_respone_time(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            elapsed_time = (end_time - start_time)

            print(f"Elapsed Time: {elapsed_time} seconds")

            return result
        return func_measue_respone_time
    return decorator_measure_response_time
