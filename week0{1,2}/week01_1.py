# print("Hello world")    #build-in function
# print "Hello world"     #statement


# print(type(1))
# print(type(1.1))
# print(type('a'))
# print(type("sad"))
# print(type(True))

# print(type([1, 3, 4]))
# [1, '11', [[['add']]]]

# d = {                   #hash table/dict
# 	'key': 1
# }
# print(d['key'])

# print(type(d))

# a = True

# if a:                  #there are no {} only spaces and that is while it's whitespace significant language
# 	if False:
# 		print('inner if')
# 	else:
# 		print('else inner')
# else:
# 	print('else')


# xs = [1, 2, 3]
# for x in xs:
# 	x = 5
# 	print(x)

# print(xs)

# for x in xs:
# 	xs[0] = x       #we can do xs = [1,21,33,3]
# 	print(x, xs)

# print(xs)
# #  ctr/ 

def key_in_dictionary(key, d):
	for d_key in d:
		if d_key == key:
			return True

	return False

c = {
	'a': 1,
	'b': 2,
	'jackpot': 40
}

# for key in c:
# 	print(key, c[key])

# for key in c:
# 	if key == 'jackpot':
# 		value = c[key]
# 		if value%2 == 0:
# 			print('YOU WIN!')


# print(key_in_dictionary('a', c))
# print('a' in c and 'b' in c)                #build-in func for list and dictionary

def all_in(xs, ys):
	for x in xs:
		if x not in ys:
			return False

	return True

# print(all_in([1,2], [1,2,3]))
# print(None)

# def f():
# 	def g():
# 	    pass
# 	g()

# f()                           #global a, nonlocal a

# def f1():
# 	print(err)

# f1()          #if f() not called than we won't use it and no error will accure

# n = 0

# while True:
# 	print(n)
# 	n+=1

# 	if n > 100:
# 		break

for x in [1,2,3]:
	if x == 2:
		continue
	print(x)
