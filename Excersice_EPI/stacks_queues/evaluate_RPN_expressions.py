from stack_max import Stack


def evaluate(exp):
    inter_res = Stack()
    delimiter = ','
    operations = {'+': lambda y,x : x+y,
                  '-': lambda y,x : x-y,
                  'x': lambda y,x : x*y,
                  '/': lambda y,x : x//y}

    for element in exp.split(delimiter):
        if element in operations:
            inter_res.push(operations[element](inter_res.pop(), inter_res.pop()))
        else:
            inter_res.push(int(element))

    return inter_res.pop()

exp = '3,4,+,3,x,1,+'
print(evaluate(exp))
