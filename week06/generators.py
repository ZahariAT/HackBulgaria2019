'''
It's not documentation, just examples/no needed functions

def panda_meals():
    yield 'Bamboo One'
    yield 'Bamboo Two'
    yield 'Bamboo Three'
    yield 'Bamboo Four'
    yield 'Bamboo Five'
    yield 'Bamboo Six'

meals = panda_meals()
for meal in meals:
    print("Num num num " + meal)
for meal in meals:
    print("Num num num " + meal)

meals2 = panda_meals()
for meal in meals2:
    print("Num num num " + meal)

def degrees(number):
    i = 2

    while i < 5:
        yield number ** i

        i += 1
        print(i)

degrees = degrees(2)
for degree in degrees:
    print(str(degree) + "\n")
    #print(degree)

def fib():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

for f in fib():
    print(f)
'''
def chain(iterable_one, iterable_two):
    for elem in iterable_one:
        yield elem
    for elem in iterable_two:
        yield elem

def compress(iterable, mask):
    iter_iterable = iter(iterable)
    for elem in mask:
        if elem:
            yield next(iter_iterable)
        else:
            next(iter_iterable)

def cycle(iterable): #who cares if it works for dictionaries
    temp = range(len(iterable))
    i = 0
    while i <= len(temp):
        if i == len(temp):
            i = 0
        yield iterable[i]
        i += 1
   
def the_real_MVP_cycle(iterable): #I do!
    iter_iterable = iter(iterable)
    while True:
        try:
            yield next(iter_iterable)
        except Exception:
            iter_iterable = iter(iterable)


import os
#import keyboard

def book_reader(a_book):
    current_chapter = ''
    for filename in os.listdir('book'): #might see the commands for this later
        with open('book/'+filename) as f:
            lines = f.readlines()
            for line in lines:
                if '#' == line[0]:
                    yield current_chapter
                    current_chapter = ''
                current_chapter += (line + ' ')
    return False

def read_chapters(a_book):
    load_chapter = book_reader(a_book)
    while load_chapter:
        pressed_key = input('Press spacebar and enter: ')
        if pressed_key == ' ':
            print(next(load_chapter))
       

import random

def book_generator(chapters_count, chapter_length_range):
    fille_with_words = open('/usr/share/dict/words')
    book_name = os.getcwd()
    try:  
        os.mkdir('book_name')
    except OSError:  
        print ('Creation of the directory %s failed' % book_name)
    else:  
        print ('Successfully created the directory %s' % book_name)
    current_count_chapter = 1
    while current_count_chapter <= chapters_count:
        word_in_chapter = random.randint(0, chapter_length_range)
        current_words = 0
        with open('book_name/' + str(current_count_chapter) + '.txt', 'a') as ch:
            ch.write('#Chapter ' + str(current_count_chapter) + '\n')
            while current_words < word_in_chapter:
                random_word = random.randint(0, 2019)
                ch.write(str(random_word) + '\n')
                current_words += 1
            current_count_chapter += 1
    fille_with_words.close()


import pyautogui
#import pynput
#import winsound  #can't install it

def current_mouse_position():
    while True:
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            print('Beep Beep')
        yield (x,y)

def some_fun():
    position = current_mouse_position()
    while input('Press enter to show the mouse position or 1 and enter to exit: ') != '1':
        print(next(position))
if __name__ == '__main__':
    some_fun()
    #print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    #print(len({1:1,2:2}))
    #print(range(0,5)[0])
    #print(len(range(len(range(0,5)))))
    #endless = the_real_MVP_cycle({}) #it works with empty, cool!
    #for item in endless:
    #    print(item)
    #print(set(chain(range(0, 4), 5)))
    #print(type(chain(range(0, 4), range(4, 8))))
    #read_chapters('book')
    #book_generator(5,5)