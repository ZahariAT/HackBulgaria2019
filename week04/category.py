class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "A person's name is {}".format(self.name)

    def __repr__(self):
        print(str(self))

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name
        return NotImplemented

class Income(Category):
    def __init__(self, name, income):
        super().__init__(name)
        self.income = income

    def __str__(self):
        return super().__str__() + " with income: {}".format(self.income)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return super().__eq__(other) and self.income == other.income
        return NotImplemented

class Expense(Category):
    def __init__(self, name, expense):
        super().__init__(name)
        self.expense = expense

    def __str__(self):
        return super().__str__() + " with expense: {}".format(self.expense)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return super().__eq__(other) and self.expense == other.expense
        return NotImplemented

b = Category("zahari")
d = Income("zahari", 45)
c = Income("zahari", 45)
a = Expense("zahari", 45)
print(a == c)
