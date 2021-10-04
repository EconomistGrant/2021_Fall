```c++
bool isOp(char ch){
    return ch == '(' || ch == ')' || ch == '+' || ch == '-' || ch == '*' || ch =='/';
}

int getPrio(char ch){
    if (ch == '('){
        return 1;
    } else if (ch == '+' or ch == '-'){
        return 2;
    } else if (ch == '*' or ch =='/'){
        return 3;
    } else{
        return 4;
    }
}

string getPostfix(string s){
    stack<char> ops;
    string Postfix;
    int n = s.size();
    for (char ch : s){
        if (ch >= '0' && ch <= '9'){
            Postfix.push_back(ch);
        } else if (isOp(ch)){
            if (ch == '('){
                ops.push(ch);
            }else if (ch == ')'){
            //if ), pop everything in the ops until (
                while(ops.empty() == false && ops.top() != '('){
                    Postfix.push_back(ops.top());
                    ops.pop();
                }
                if (ops.top() == '('){
                    ops.pop();
                }
            } else if (ops.empty() || getPrio(ch) > getPrio(ops.top())) {
            //push in the temp stack if a) stack is empty or 
            //b) having strictly larger prio than the top as it will be calculated first
                ops.push(ch);
            } else {
            //top of the stack will be calculated first, pop and append to the end
                while (ops.empty() == false && getPrio(ch) <= getPrio(ops.top())){
                    Postfix.push_back(ops.top());
                    ops.pop();
                }
                ops.push(ch);
            }
        }
    }
    while (ops.empty() == false){
        Postfix.push_back(ops.top());
        ops.pop();
    }
    return Postfix;
}
```

```python
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
                post_fix.append(temp_value)
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
```