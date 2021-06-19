''' Example python file'''

from decorators import exception_handler
from decorators import measure_response_time
import time

@exception_handler()
def example_function(a):
    ''' DocString '''
    return 66/a

example_function(317)
example_function(0)
example_function("any_type_of_str")

@measure_response_time()
def example_function_2(last_words):
    ''' DocString '''
    time.sleep(3)
    print(last_words)
    return last_words

example_function_2("I'm only sleeping")
