from stack_max import Stack


def valid_parenthesis(par):
    s = Stack()
    pairs = {'(': ')', '[':']', '{': '}'}
    for p in par:
        if p in pairs:
            s.push(p)
        elif s.empty() or pairs[s.pop()] != p:
                return False
    return not s.empty()

a = '()[]{}'
b = '[{)){[}'

print(valid_parenthesis(a))
