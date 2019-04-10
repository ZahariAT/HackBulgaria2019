#tuple a = 1, === b = (1, )
user = ('Mimi', 24, 'Sofia')
username, age, addres = user

#print(age)

def gas_stations(distance, tank_size, stations):
    shortest_list = []
    temp = tank_size

    i = 0
    while i < len(stations):
        if temp < stations[i]:
            shortest_list.append(stations[i-1])
            temp = stations[i-1] + tank_size

        i += 1

    if temp < distance and temp >= stations[i - 1]:
        shortest_list.append(stations[i - 1])

    
    print(shortest_list)

#gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])

def gas_stations2(distance, tank_size, stations):
    gas_stations_it_route = []
    distance_traveld = 0
    while distance_traveld + tank_size < distance:
        gas_station = max([station for station in stations if station <= distance_traveld + tank_size])
        gas_stations_it_route.append(gas_station)
        distance_traveld = gas_station

    print(gas_stations_it_route)

#gas_stations2(390, 80, [70, 90, 140, 210, 240, 280, 350])

def is_number_balanced(n):
    string = str(n)
    ints = [int(char) for char in string]
    length = len(ints)
    skipp_middle_index = 1 if length % 2 == 1 else 0
    return sum(ints[:length//2]) == sum(ints[(length//2 + skipp_middle_index):]) or length == 1   # lst[len(lst):] = [smth] === lst.append(smth)
                                                                 #lst[from:to:with_step]    if with_step is negatife than the list gets reversed

#print(is_number_balanced(28491))

def increasing_or_decreasing(seq):
    lst = seq[1:]
    is_incr = all([lst[lst_index] > seq[lst_index] for lst_index in range(len(lst))])  #it can be made with zip
    is_decr = all([lst[lst_index] < seq[lst_index] for lst_index in range(len(lst))])
    
    if is_incr:
        return 'Up!'
    if is_decr:
        return 'Down!'
    return False

#print(increasing_or_decreasing([1,2,3,4,5]))

import re            #library working with regular expressions
#(r'd', 'asd123dfsd56') -> [123,56]    #d for digits === '0-9'

def sum_of_numbers(input_string):  #isdigit() is a valid solution
     list_of_numbers = re.findall(r'\d+', input_string)                          #use reg expr
     return sum([int(elem) for elem in list_of_numbers])

#print(sum_of_numbers('sdervf123wf3d'))

def birthday_ranges(birthdays, ranges):
    result = []
    for a_range in ranges:
        counter = 0
        for birthday in birthdays:
            if birthday in range(a_range[0], a_range[1] + 1):
                counter += 1
        result.append(counter)

    return result

#print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))

#use dictionary for sms

def numbers_to_message(pressed_sequence):
    pass

def message_to_numbers(message):
    pass

def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    result = 0
    if people_floors == [] or people_weight ==[]:
        return 0
    
    i = 0
    _from = 0
    length = len(people_weight)
    #print(length)
    while i < length:
        j = 1
        temp_weight = 0

        while j <= max_people and i < length:
            j += 1
            temp_weight += people_weight[i]
            if temp_weight > max_weight:
                break
            i += 1
        temp_floors = people_floors[_from:i]
        #print(i)
        #print('f', _from)
        while _from < i - 1:
            if temp_floors[_from] != temp_floors[_from + 1]:
                result += 1
            _from += 1
        #print('f2', _from)
        _from = i
        result += 2
        #print('r ',result)
    return result

#print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))  #not sure why it doesn't work

def elevator_trips2(people_weight, people_floors, elevator_floors, max_people, max_weight):
    #todo if/exceptions
    trips = 0
    current_weight = 0
    start_index = 0
    for index, person_weight in enumerate(people_weight):
        current_weight += person_weight
        if current_weight > max_weight or len(people_weight[start_index:index]) >= max_people:
            trips += len(set(people_floors[start_index:index])) + 1
            current_weight = person_weight
            start_index = index
    trips += len(set(people_floors[start_index:])) + 1
    return trips

#print(elevator_trips2([80, 60, 40], [2, 3, 5], 5, 2, 200))

def elevator_trips3(people_weight, people_floors, elevator_floors, max_people, max_weight):
    trips = 0
    while len(people_weight) > 0:
        current_floors = [people_floors[index] for index, person in enumerate(people_weight) if sum(people_weight[:index + 1]) <= max_weight and len(people_floors[:index + 1]) <= max_people]
        trips += len(set(current_floors)) + 1
        people_weight = people_weight[len(current_floors):]
        people_floors = people_floors[len(current_floors):]
    return trips

#print(elevator_trips3([80, 60, 40], [2, 3, 5], 5, 2, 200))


def anagrams():
    print('Enter 2 words:')
    word1 = input()
    word2 = input()
    result = [char for char in word1.lower() if char in word2.lower()]
    if len(result) == len(word2) and len(result) == len(word1):
        return 'Anagrams'
    return 'NOT Anagrams'

#print(anagrams())
import math

def is_credit_card_valid(number):
    str_number = str(number)
    if len(str_number) % 2 == 0:
        return False
    lst_number = [int(char) for char in str_number]
    odd_indexes = [2*elem for elem in lst_number[len(lst_number) - 2::-2]]
    even_indexes = lst_number[::-2]
    str_odd = ''
    for odd_indexe in odd_indexes:
        str_odd += str(odd_indexe)
    odd_indexes = [int(char) for char in str_odd]
    return (sum(odd_indexes) + sum(even_indexes)) % 10 == 0

#print(is_credit_card_valid(79927398713))

def goldbach(n):
    lst_prime = []
    for prime in range(2, n):
        if all(prime % i for i in range(2, int(math.sqrt(prime))+1)):
            lst_prime.append(prime)
    return [(x, y) for x in lst_prime for y in lst_prime if x + y == n and x <= y]

#print(goldbach(52))
