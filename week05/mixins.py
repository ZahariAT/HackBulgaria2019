import json
import xml.etree.ElementTree as ET

class Jsonable:
    def to_json(self, indent=4):
        #str_type = str(self.__class__).split('.')[1].split("'")[0]
        return json.dumps({'dict':self.__dict__, 'type':self.__class__.__name__}, indent=indent)

    @classmethod 
    def from_json(cls, json_string):
        obj = cls()
        if json.loads(json_string)['type'] != cls.__name__:
            raise TypeError
        for k, v in json.loads(json_string)['dict'].items():
            setattr(obj, k, v)
        return obj

class Xmlable:
    def to_xml(self):
        self_dict = self.__dict__.items()
        tree = ET.Element(self.__class__.__name__)
        for tag, text in self_dict:
            node = ET.Element(tag)
            node.text = str(text)
            tree.append(node)
        return ET.tostring(ET.ElementTree(tree).getroot())

    @classmethod
    def from_xml(cls, xml_string):
        obj = cls()
        tree = ET.fromstring(xml_string)
        if tree.tag != cls.__name__:
            raise TypeError
        for node in tree:
            if node.text.isdigit():
                setattr(obj, node.tag, int(node.text))
            else:
                setattr(obj, node.tag, node.text)
        return obj


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.__dict__ == other.__dict__
        return NotImplemented

if __name__ == '__main__':
    p = Panda(name='iv',age=22)
    p1 = p.to_json()
    #print(type(p1))
    print(p.to_xml())
    p2 = Panda.from_json(p1)
    p3 = Panda.from_xml(p.to_xml())
    print(p3)
    print(p2)
    print(p2 == p)
    print(p2 == p3)
    #print(Panda(name='z', age={'1':1, '2':2}).to_json())
    #print(Panda.from_json(Panda(name='z', age={'1':1, '2':2}).to_json()))
    