x = None
print(x)

x = 134134.1414124
print(type(x))


x = [1,2132,4,142,1,41,41]
print(x)

for y in x:
    print(y)


def my_function():
    p = 23.1341431
    print(p / 2.0)


my_function()


x = 2
y = 5
if(x == 2 or y == 5):
    print("We are int")
else:
    print("almost we did it")

x = False
if(x == (not True)):
    print("ok")

a = (1,2,3)
print(a)

a = "123"
b = int(a)


dict = {
    "one":1,
    "two":2,
    "three":3
}

for k in dict:
    print("{} is {}", format(k,dict[k]))