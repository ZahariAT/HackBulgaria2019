print("Hello World")

a = min(1,2,123,-3)

print(a + 2)


# missing semi-colons and data types, Python is dynamicly typed
# languages, aka it is not neccassiry to specify the type of a variable


print(type(a))

#there isn't char in python, aka '' == ""

print(type([1,2,3])) #list 




# dictionary

d = {
    'key':1
}


b = [1,21,3,142,214]
print(d)
print(d['key'])

print(b)


# WHITE SPACE SIGNIFICANT LANGUAGE , NO NEED OF {} !!!!!!!!!!!!!!!!

a = True 

if(a):
    print(a)


for x in b:
    b[0] = x
    print(x)

print(b)


d = {
    'key' : 1,
    'a' : 2,
    'jackpot':40
}

for key in d:

    if(key == 'jackpot'):
        
        value = d[key]
        if(value % 2 == 0):
            print("haha")
    print(key,d[key])



def key_in_dictionary(key,d):
    for d_key in d:
        if(d_key == key):
            return True
    return False


print(key_in_dictionary(3,d))


print('a' in d)
print('c' in d)


def all_in(thingsToCheck,toBeChecked):
    for x in thingsToCheck:
        if(x not in toBeChecked):
            return False
    return True


print(all_in([1,2,3],[1,2,5,6]))

# None == null

print(None)


# pass -- nothing in the body of the function 


def f():
    global a
    def g():
        
        a = 20
    g()
    a = 10
    print(a)

f()


commands_we_know  = ["pwd","ls","cat","python"]