class Contract:
    def __init__(self, car, person, money):
        self.car = car
        self.person = person
        self._money = money

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value):
        self.money = value