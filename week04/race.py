import json
import random #random.uniform(0,1)
import sys
import os

with open('cars.json') as f:
    data = json.load(f)
#print(data)
other_data = dict()
class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return str(self.max_speed)

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return self.max_speed > other.max_speed
        return NotImplemented

class Driver:
    def __init__(self, name, car):
        self.driver_name = name
        self.driver_car = car

    def __str__(self):
        return self.driver_name

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return self.driver_car.__gt__(other.driver_car)
        return NotImplemented

class Race:
    def __init__(self, drivers, crash_chance):
        self.drivers = drivers
        self.crash_chance = crash_chance

    def result(self):
        sorted_drivers_by_speed = sorted(self.drivers, reverse=True)
        #sorted_speed_paired_with_random_number = [(speed, random.uniform(0,1)) for speed in sorted_by_speed]
        crashed_drivers = list()
        not_crashed_drivers = list()
        for elem in sorted_drivers_by_speed:
            if random.uniform(0,1) < self.crash_chance:
                crashed_drivers.append(elem)
            else:
                not_crashed_drivers.append(str(elem))
        points = [8, 6, 4]
        for i in range(min(len(not_crashed_drivers), len(points))):
            if not_crashed_drivers[i] in other_data.keys():
                other_data[not_crashed_drivers[i]] += points[i]
                print(str(not_crashed_drivers[i]), " - ", str(points[i]))
            else:
                other_data[str(not_crashed_drivers[i])] = points[i]   #str(driver) equals driver.name
        print(str(other_data))
        for the_unfortunate in crashed_drivers:
            print("Unfortunately, {} has crashed.".format(the_unfortunate))

    def __str__(self):
        return str(self.drivers)

    def __repr__(self):
        return str(self)


class Championship:
    def __init__(self, name, races_count):
        self.race_name = name
        self.races_count = races_count

def some_func_that_should_be_a_class():
    lst_drivers = list()
    for elem in data['people']:
        a_car = Car(elem['car'], elem['model'], elem['max_speed'])
        a_driver = Driver(elem['name'], a_car)
        lst_drivers.append(a_driver)
    passed_arg = sys.argv
    if passed_arg[1] == "start":
        print("Starting a new championship called {0} with {1} races.".format(passed_arg[2], passed_arg[3]))
        for i in range(int(passed_arg[3])):
            print('\n', "=====START=====", '\n')
            Race(lst_drivers, random.uniform(0,1)).result()
        result_dict = {}
        if os.stat("result.json").st_size == 0:
            with open('result.json', 'w') as f:
                json.dump({passed_arg[2]:[other_data]}, f, indent=2)
        else:
            with open('result.json') as f:
                result_dict = json.load(f)
            if result_dict == None:
                result_dict = {}
            with open('result.json', 'w') as f:
                result_dict.update({passed_arg[2]:[other_data]})
                json.dump(result_dict, f, indent=2)

if __name__ == '__main__':
    some_func_that_should_be_a_class()
'''
I haven't opened this file for ages and have no idea how it works 
and have no time to learn again, so will skip it. 
The main functionality shoud be here even though not in the correct form.
'''