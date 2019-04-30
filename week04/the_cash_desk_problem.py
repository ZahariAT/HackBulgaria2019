class Bill:
    #self is the pointer to the current_obj and with self. we give him attributes, not neccesery to be that name but it's the first param of __init__
    def __init__(self, bill):
        self.validate_init_params(bill)
        self.curr_bill = bill

    def validate_init_params(self, bill):
        if type(bill) is int:
            pass
            #print('Panda name is valid')
        else:
            raise ValueError

    def __int__(self):
        return self.curr_bill

    def __str__(self):
        return "A {}$ bill".format(self.curr_bill)

    def __repr__(self):
        print(str(self))

    def __eq__(self, other):
        return self.curr_bill == other.curr_bill

    def __hash__(self):
        return hash(self.curr_bill)


class BillBatch:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum(int(bill) for bill in self.bills)

class CashDesk:
    _smth = list()

    def take_money(self, money):
        if type(money) is Bill:
            self._smth.append(money)
        elif type(money) is BillBatch:
            self._smth += money
        else:
            raise ValueError

    def total(self):
        return "We have a total of {}$ in the desk".format(sum(int(elem) for elem in self._smth))

    def inspect(self):
        a_dict = {}
        for bill in self._smth:
            temp = int(bill)
            if temp in a_dict.keys():
                a_dict[temp] += 1
            else:
                a_dict[temp] = 1
        print(sorted((k, v) for k, v in a_dict.items()))

if __name__ == '__main__':
    bill = Bill(10)
    bill2 = Bill(10)
    '''
    print(str(bill))
    print(bill)
    print(bill == bill2)
    '''
    money_holder = {}

    money_holder[bill2] = 1 # We have one 10% bill

    if bill in money_holder:
        money_holder[bill2] += 1

    #print(money_holder) # { "A 10$ bill": 2 }... doesn't work

    from collections import OrderedDict

    #print(list(OrderedDict.fromkeys(t)))


    values = [50, 10, 10, 50, 100]
    bills = [Bill(value) for value in values]
    #for bill in bills:
        #print(bill)
    batch = BillBatch(bills)
    #print(batch.total())
    #for bill in batch:
     #   print(bill)
    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))
    print(desk.total())
    desk.inspect()
    #we have objName.__dict__
