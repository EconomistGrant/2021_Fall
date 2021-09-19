# Introduction to Predictive Analytics and Data Architecture

# Recap index?
weighted acerage of basket of stocks
Derivation: P6
Divisor: changes to make index smooth

# Predictive Analytics & Statistical Arbitrage
observe patterns that we think normal, can be used to predict future
quantitative trading sstrategy: efficient market hypothesis, paradoxical, if information properly anticipated

# A trading strategy
weight = negative of excess return
$$w_i(t) = -c(R_i(t) - \bar{R})$$
$$\pi(t) = \sum_{i=1}^N w_i(t-1)R_i(t)$$
$$R(t) = \frac{P_t}{P_t - P_{t-1}}$$

# Backtest
numerical simulation of a trading strategy or algorithm 
using historical data

theory vs reality vs simulation

# Data architecture and data modeling
entities and relationships?
how do we represent, store, and analyze multivariate data

# Data Modelling
desribes informatopm structires amd relationships

"above the line": uniquely determine 

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