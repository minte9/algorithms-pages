import time
import sys
sys.dont_write_bytecode = True # no .pyc

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        print(func.__name__ + "():\t", time.time() - t1, "s")
        return res
    return wrapper