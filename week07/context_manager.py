from contextlib import ContextDecorator
from contextlib import contextmanager
from datetime import datetime
from time import sleep, time
#import timeit

'''
-------examples-------

class Context:
    def __init__(self):
        print('init')
        self.prop = 1

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, *argv):
        print('exit')

def generate():
    with Context() as cm:
        res = 42
        print('CM instance: ', cm)
    return res

#generate()

@contextmanager
def context():
    print('enter')

    yield 43

    print('exit')

@contextmanager
def timed():
    """A simple timer context manager, implemented using a generator function"""
    start = time()
    print("Staring at {}".format(start))

    yield

    end = time()
    print("Ending at {} (total: {})".format(end, end - start))

with timed() as t:
    sleep(1)
    print(t)
'''

@contextmanager
def performance(file_name):
    start = time()

    yield

    end = time()
    if end - start > 1:
        with open(file_name, 'a') as f:
            f.write('Date {}. Execution time: {}\n'.format(datetime.now(), end-start))

#with performance('log_file.txt'):
#    sleep(1)

@contextmanager
def assertRaises(exception, msg=None):
    print('in enter')

    try:
        yield
        raise print('exception not found')
    except Exception as exc:
        if type(exc) == exception:
            if msg is not None or not str():
                print(msg)
                return True
            else:
                raise Exception('message not correct')
        raise Exception('is found but not ours')

def my_sum(num1, num2):
    if num1 < 0 or num2 < 0:
        raise TypeError
    return num1 + num2

with assertRaises(TypeError, 'smth'):
    my_sum(-1,2)
