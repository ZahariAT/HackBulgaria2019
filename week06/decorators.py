import datetime
from functools import wraps
import time
import timeit
#kolko funkcii za vreme ima, basi

def accepts(*types):
    def accepter(func):
        def check_types(*argv):
            for i in range(len(types)):
                if type(argv[i]) != types[i]:
                    raise TypeError
            return func(*argv)
        return check_types
    return accepter

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

def encrypt(key):
    def accepter(func):
        @wraps(func)
        def decorator(*argv):
            string = func(*argv)
            smth = [[char for char in word] for word in string.split(' ')]
            smth_encrypt = [[chr(ord(char) + key) for char in word] for word in smth]
            return ' '.join([''.join(word) for word in smth_encrypt])
        return decorator
    return accepter

def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorator(*argv):
            with open(file_name, 'a') as destin:
                destin.write('{} was called at {}\n'.format(func.__name__, datetime.datetime.now()))
            return func(*argv)
        return decorator
    return accepter

@log('log.txt')
@encrypt(2)
def get_low():
    return 'Get get get low'

def performance(file_name):
    def accepter(func):
        @wraps(func)
        def decorate(*argv):
            with open(file_name, 'a') as f:
                f.write('{} was called and took {} seconds to compile\n'.format(func.__name__,timeit.timeit(func, number=1)))
            return func(*argv)
        return decorate
    return accepter

@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return 'I am done!'

if __name__=='__main__':
    #deposit("Roza", 10)
    #print(say_hello("Hacker"))
    print(get_low())
    print(something_heavy())
    print(timeit.timeit(something_heavy, number=1)) #cuz of decorator calling the func and then we call func and that's why it actually takes double time to run the func with decorater

#print(get_low())