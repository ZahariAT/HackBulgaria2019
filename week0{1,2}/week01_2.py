#REPL (read, evaluate, print, loop)
# def sum3(a, b, c):
#     return a+ b+ c

# print(sum3(1, 2 , 3))


#from filename import somethink(funk, const, var)
#list + list === concat
#explicit type casting (1 + '1' is invalid)
#everything is object
# listname.append(value) is mutator
#listname += [value]


# a = [1, 2, 3]
# print(len(a))                  #build-in func

# items = ['a', 'b', 'c', 'd']
# indexes = range(len(a))

# for index in indexes:
#     item = items[index]
#     print(item)

def sum_of_digits(n):
    sum = 0

    if (n < 0):
        m = -n
    else:
        m = n

    while(m > 0):
        sum += m%10
        m = m // 10

    return sum

#print(sum_of_digits(1234))

def my_reverse(xs):
    indexes = range(len(xs))
    rev_xs = []
    length = len(xs)

    for index in indexes:
        rev_xs.append(xs[length - index - 1])

    return rev_xs

#print(my_reverse([1,2,3]))



def to_digits(n):
    a = []
    if (n < 0):
        m = -n
    else:
        m = n

    while(m > 0):
        a.append(m % 10)
        m = m // 10

    a.reverse()
    return a

#print(to_digits(123))


def to_number(xs):
    string = ''

    indexes = range(len(xs))        #better just for x in xs
    for index in indexes:           # #that construction(signature) is called list comprehension and it can be made by map or [g(arg) for arg in args]
        string += str(xs[index])

    return int(string)

#print(type(to_number([1,3,4])))

def fact_digits(n):
    def fact(n):
        if n == 0:
            return 1

        return n*fact(n-1)

    sum = 0
    while (n != 0):
        sum += fact(n%10)
        n //= 10

    return sum

#print(fact_digits(999))

def count_vowels(str):
    indexes = range(len(str))
    counter = 0
    for i in indexes:
        if (str[i] == 'a' or str[i] == 'e' or str[i] == 'o' or str[i] == 'u' or str[i] == 'i' or str[i] == 'y'):
            counter += 1


    return counter

#print(count_vowels("Theistareykjarbunga"))

def sum_of_digits2(n):      # like in Haskel
    n = abs(n)

    digits = [int(ch) for ch in str(n)]

    return sum(digits)

#print(sum_of_digits2(123))

d = [[x, x] for x in {'a': 1, 'b': 2} if x != 'a']
#print(d)

def join(items, delimiter):    #build-in func
    result = ''
    n =len(items)

    for i in range(n):
        item = items[i]

        result += item

        if i < n:
            result += delimiter

    return result

def to_number2(digits):
    chars = [str(digit) for digit in digits]

    return int(join(chars, ''))

#print(to_number2([1,2,3]))


def char_histogram(string):
    result = {}

    for ch in string:
        if ch not in result:
            result[ch] = 1     #dictionary[key] === value
        else:
            result[ch] += 1

    return result

#print(char_histogram('aadd'))

def sum_matrix(m):
    return sum([sum(elem) for elem in m])

#print(sum_matrix([[1,2,3],[1,2,3]]))

def nan_expand(times):
    if times == 0:
        return ""
    else:
        indexes = range(times)
        result = ''
        for i in indexes:
            result += 'Not a '
        result += 'NaN'
        return result

#print(nan_expand(3))

def prime_factorization(n):
    pass

def group(xs):
    pass

#dictionaryname.get(key,if_key_not_in_dict_return_this__else_value)