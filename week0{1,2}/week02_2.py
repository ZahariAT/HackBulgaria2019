'''
__name__ = '__main__'     # === our main file

from helper02_2 import smth1, smth2

#from filename import *       === import evrth

#import how_file
#how_file.smth

print(smth2(2, 3))

def main():      #for convention it's called main
    print("in week02_2")

if __name__ == '__main__':
    main()
'''

'''
f = open('helper.txt', 'r')      # 'r' - read, 'w' - write , 'a' - append, 'r+' - read and write
print(f.readlines())
f.close()

with open('helper.txt', 'r') as f:
    print(f.readlines())

#the moment we get out from the block it altomatically closes the file
'''

# 2 types of errors - syntaxis and exceptions

'''try:
    user_age = int(input('Your age: '))
except:
    pass
else:
    pass
finally:
    pass
'''
'''try:
    rositsa = 'Rosica'
    user_name = rositsa + "Zlateva"
    f = open(input(), 'r')
    f.readlnes()

    #print(1 / 0)
#except (ZeroDivisionError, NameError) as exc:
#    print(exc)
#except TypeError as exc:
#    print("Smth else")

except Exception as exc:
    print(exc)
#    raise RuntimeError
else:
    print("in else")
finally:
    print('in finally')
    f.close()
'''

# cat.py
import sys

def cat(arguments):
    with open(arguments, 'r') as f:
        print(f.readlines())

def cat2(arguments):
    for argument in arguments[1:]:
        cat(argument)

from random import randint

def generate_numbers(filename, numbers):
    with open(filename, 'w') as f: 
        for i in range(numbers):
            f.write(str(randint(1, 1000)))
            f.write(' ')

import re
def sum_numbers(filename):
    with open(filename, 'r') as f:
        lst = f.readlines()
        string = lst[0]
        result = sum([int(char) for char in re.findall(r'\d+', string)])
        #string.split(" ")  #-> returns a list
        #sum(map(int, string))
    return result

def chars(line):
    number = 0
    result = ''
    lst_symbols = re.findall(r'[a-zA-Z]*', line)
    print(lst_symbols)
    for symbol in lst_symbols:
        result += symbol
    return len(result)

def wc(filename, func):
    result = 0

    with open(filename, 'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            result += eval(func)(line)
    return result

def reduce_file_path(path):
    splited_path = path.split('/')
    print(splited_path)
    for index in range(len(splited_path)):
        if splited_path[index] == '.':
            splited_path[index] = ''
        if splited_path[index] == '..':
            splited_path[index] = ''
            splited_path[index - 1] = ''
    splited_path = ["/" + elem for elem in splited_path if elem != '']
    result = ''
    for elem in splited_path:
        result += elem
    if len(splited_path) == 0:
        result = '/'
    return result

import os 

def du_hs(paths):
    files_in_directory = []
    for (dirpath, dirnames, filenames) in os.walk(paths):
        for file in filenames:
                files_in_directory.append(os.path.join(dirpath, file))


    files_size = 0
    for files in files_in_directory:
        files_size += int(os.path.getsize(files))

    print(round((float(files_size / 1024)), 2), end = '')
    print("kB")


def main():
    #data = sys.argv[1]
    #cat(data)
    #data2 = sys.argv
    #cat2(data2)
    #data3 = sys.argv
    #generate_numbers(data3[1], int(data3[2]))
    #data4 = sys.argv[1]
    #print(sum_numbers(data4))
    #data6 = sys.argv
    #print(wc(data6[2], data6[1]))
    #print(reduce_file_path("/../"))
    du_hs(sys.argv[1])

if __name__ == '__main__':
    main()