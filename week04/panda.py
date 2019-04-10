class Panda:
    current_panda = "Rado"
    #self.validate_init_params(name, food, weight)
    def __init__(self, name, food, weight):        
        self.panda_name = name
        self.fav_food = food
        self.curr_weight = weight

      #  for k, v in kwargs.items(): if we had **kwargs
       #     setattr(self, k, v)

    def validate_init_params(self, name, food, weight):
        if name is str:
            print('Panda name is valid')
        else:
            raise ValueError
    def __eq__(self, other):
        return True

    def celebrate_birthday(self):
        self.curr_weight += 1

    def __str__(self):
        return "Panda: {0}".format(self.panda_name)


panda_ivo = Panda('Ivo', 'ice-cream', 74)
#print(panda_ivo.panda_name)
#print(panda_ivo.curr_weight)
#print(panda_ivo.fav_food)
#panda_ivo.celebrate_birthday()          # same
#Panda.celebrate_birthday(panda_ivo)     #
#print(panda_ivo.curr_weight)
#print(panda_ivo == panda_ivo)           # defoult equal
#print(panda_ivo is panda_ivo)

panda_ivo2 = Panda('Ivo', 'ice-cream', 74)
#print(panda_ivo2 == panda_ivo)
#print(panda_ivo2 is panda_ivo)              #to work we have to make our own equal; is is the original equal for objects

# dunder === double == magic methods under __smth__
panda_ivo.current_panda = "Rosi"
print(panda_ivo.current_panda)