from functools import wraps
from time import time


def timeit(func):
    @wraps(func)
    def timed_func(*args, **kwargs):
        time_in = time()
        result = func(*args, **kwargs)
        time_spent = time() - time_in

        return time_spent, result

    return timed_func
