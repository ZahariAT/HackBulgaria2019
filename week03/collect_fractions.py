import math

def simplify_fraction(fraction):
    if not isinstance(fraction,tuple):
        raise ValueError('Not a tuple')
    if fraction[1]==0:
        raise ZeroDivisionError('Divison by zero!')
    gcd = math.gcd(fraction[0], fraction[1])
    return (fraction[0]/gcd, fraction[1]/gcd)

def collect_fractions(fractions):
    if not isinstance(fractions, list):
        raise ValueError('Not a list')
    for fraction in fractions:
        if not isinstance(fraction,tuple):
            raise ValueError('Not a tuple')
        if fraction[1] == 0:
            raise ZeroDivisionError('Divison by zero!')
    fst, scd = fractions
    return simplify_fraction((fst[0]*scd[1] + fst[1]*scd[0], fst[1]*scd[1]))

#print (collect_fractions([(1,0),(1,2)]))

def sort_fractions(fractions):
    if fractions == []:
        return []
    return sorted(fractions, key = lambda x: x[0]/x[1])
print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

'''
def func(par, par2, def_par = 1):
    pass
func(1, 2), func(1, 2, 3), func(par2=3, def_par=4, par2=2) but it can't be func(par2=1, 3, 4)


def sum_of_numbers(*args):
    return sum(args)
args is a tuple

sum_of_numbers(1, *(1,2,3))

def func(arg1, args*):
    arg1 is smth and args is a tuple of smths

def sum_of_numbers(num1, **kwargs):
    return num1 + sum(kwargs.value())
kwargs is a dictionary

sum_of_numbers(1, **{'num2': 3}) -> 1+3 = 4

vars live beyond there scopes
'''