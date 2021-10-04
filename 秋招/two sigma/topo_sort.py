##################################################
# directed accyclical graph
# u -> v, v finishes dfs before u
##################################################
import sys

# DO NOT REMOVE THIS LINE
sys.setrecursionlimit(100000)

def DFS(v,dependencies):
    """
    do bfs and return the order of v
    """
    global order,status
    #0 undiscovered, 1 unfinished, 2 finished
    if status[v] == 2: 
        return order[v]
    if status[v] == 1: 
        raise RuntimeError
    
    status[v] = 1
    prerequisites = dependencies[v]
    pre_max = 0

    for node in prerequisites: 
        pre_max = max(pre_max,DFS(node, dependencies))
    
    order[v] = pre_max+1
    status[v] = 2
    return order[v]

        
def determine_install_order(dependencies):
    """
    Args: 
        dependencies (list): adjacency list showing which libraries each library is dependent on

    Output:
        int: The minimum number of sessions needed to install all libraries or None if there is no valid install order
    """
    global order, status
    order = [0] * len(dependencies)
    status = [0] * len(dependencies) #0 undiscovered, 1 unfinished, 2 finished
    if len(dependencies) == 0: return 0
    for v in range(len(dependencies)):
        try:    DFS(v,dependencies)
        except: return None
        
    return max(order)