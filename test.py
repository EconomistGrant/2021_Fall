def is_operation(ch):
    return ch == '(' or ch == ')' or ch == '+' or ch == '-' or ch == '*' or ch =='/'

def get_priority(ch):
    if ch == '(':
        return 1
    elif ch == '+' or ch == '-':
        return 2
    elif ch == '*' or ch == '/':
        return 3
    else:
        return 4

def get_postfix(string):
    ops = []
    postfix = []
    temp_value = 0
    n = len(string)
    for idx, char in enumerate(string):
        if not is_operation(char):
            temp_value = temp_value*10+int(char)
            if idx < n-1 and is_operation(string[idx+1]) == False:
                continue
            else:
                postfix.append(temp_value)
                temp_value = 0
        elif char == '(':
            ops.append(char)
        elif char == ')':
            while ops[-1] != '(':
                postfix.append(ops.pop())
            ops.pop()
        elif len(ops) == 0 or get_priority(char) > get_priority(ops[-1]):
            ops.append(char)
        else:
            while len(ops) > 0 and get_priority(char) <= get_priority(ops[-1]):
                postfix.append(ops.pop())
            ops.append(char)
    
    while len(ops) > 0:
        postfix.append(ops.pop())
    return postfix

print(get_postfix("87+(45-6)*2"))