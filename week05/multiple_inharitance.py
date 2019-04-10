class A:
    pass

class B(A):
    pass

class C(A):
    pass


class M(B, C):
    pass

from pprint import pprint
pprint(M.mro())   #return list
pprint(M.__mro__) #return tupel
#pprint(M.__dir__)