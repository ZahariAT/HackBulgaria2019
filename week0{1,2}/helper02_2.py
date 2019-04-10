import sys

def smth1():
    print('smth1')

def smth2(a, b):
    return a + b

if __name__ == '__main__':
    arguments = sys.argv
    print(arguments)
    print("in helper ")