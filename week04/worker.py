class Worker:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def salary(self):
        return self._salary

class Tailor(Worker):
    def __init__(self, name, address, salary):
        super().__init__(name, salary)  #super() takes __init__ from Worker
        self.tailor_address = address

    @classmethod
    def f(cls, attribute):    #cls(attribute) === Tailor(attribut)
        pass

    @staticmethod
    def g():
        pass

    def h(self):
        pass
