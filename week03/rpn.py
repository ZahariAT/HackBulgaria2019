import math

def rpn_calculater(number):
    split_expr = number.split(' ')
    if len(split_expr) == 1:
        return int(split_expr[0])
    operator = split_expr[2]
    if operator == '-':
        return int(split_expr[0]) - int(split_expr[1])
    if operator == '+':
        return int(split_expr[0]) + int(split_expr[1])

def rpn_calculate(number):
    split_expr = number.split(' ')
    if len(split_expr) == 1:
        return int(split_expr[0])
    result = 0
    for i in range(len(split_expr)):
        if split_expr[i] not in ['1', '2' , '3', '4', '5', '6', '7', '8', '9', '0']:
            if split_expr[i] == 'SQRT':
                result = math.sqrt(int(split_expr[i-1]))
                split_expr[i - 1] = split_expr[i - 2]
            else:
                result = eval(split_expr[i - 2] + split_expr[i] + split_expr[i - 1])
                split_expr[i - 1] = split_expr[i - 3]
            split_expr[i] = str(result)
    return result
