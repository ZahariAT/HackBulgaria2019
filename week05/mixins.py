import json

class Jsonable:
    def to_json(self, indent=4):
        #str_type = str(self.__class__).split('.')[1].split("'")[0]
        return json.dumps({'dict':self.__dict__, 'type':self.__class__.__name__}, indent=indent)

    @classmethod 
    def from_json(cls, json_string):
        obj = cls()
        if json.loads(json_string)['type'] != obj.__class__.__name__:
            raise TypeError
        for k, v in json.loads(json_string)['dict'].items():
            setattr(obj, k, v)
        return obj

class Xmlable:
    pass


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.__dict__ == other.__dict__
        return NotImplemented

#from pprint import pprint

p = Panda(name='iv',age=2)
p1 = p.to_json()
#print(type(p1))
p2 = Panda.from_json(p1)
print(p2 == p)
#print(Panda(name='z', age={'1':1, '2':2}).to_json())
#print(Panda.from_json(Panda(name='z', age={'1':1, '2':2}).to_json()))
#pprint(dir(Panda('a',3)))