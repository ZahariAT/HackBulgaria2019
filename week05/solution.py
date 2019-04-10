class SingleArgument:
    def __init__(self, expr):
        if type(expr) is not str:
            raise TypeError('Expecting a string type but {} is given'.format(type(expr).__name__))
        self.expr = expr

    def derivate(self):
        if 'x' not in self.expr:
            return '0'
        multiplayer_exponend = self.expr.split('x')
        if multiplayer_exponend[0] == '':
                multiplayer_exponend[0] = '1'
        if multiplayer_exponend[1] == '':
            return multiplayer_exponend[0]
        if multiplayer_exponend[1][1] == '2':
            return str(eval(multiplayer_exponend[0]+ '*' + multiplayer_exponend[1][1])) + 'x'
        return str(eval(multiplayer_exponend[0]+ '*' + multiplayer_exponend[1][1:])) + 'x^' + str(int(multiplayer_exponend[1][1:]) - 1)

class Polynom:
    def __init__(self, polynom):
        self.polynom = polynom
    
    def polynom_derive(self):
        derivate_polynom = [SingleArgument(var).derivate() for var in self.polynom.split('+') if 'x' in var]
        if derivate_polynom == []:
            return '0'
        return '+'.join(derivate_polynom)






print(Polynom('3').polynom_derive())