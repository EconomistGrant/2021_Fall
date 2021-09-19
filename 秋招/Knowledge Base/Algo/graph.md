General unweighted | BFS | V + E
DAG +/-            | DAG | V + E
General non-nega   |Dijk | VlogV + E
General +/-        |BF   | VE
APSP               |Jhons| V^2logV + VE  ---Dijstra * V

# BFS
mark **unmarked** neighbors i+1 for *vertices marked with i*
create and maintain a **marked i** list => shortest path from orgin
# DFS
tree edge
to discovered but unfinished: back edge
to finished & earlier visited: cross edge (undirected: will be tree edge)
to finished & later visited: forward edge (undirected: will be back edge)

# DAG
DFS, when backtrack assign a number
topological sort: if u -> v, TS(u) < TS(v)
```python
def DFS(v,dependencies):
    """
    do bfs and return the order of v
    """
    global order,status
    if status[v] == 2: return order[v]     #finished
    if status[v] == 1: raise RuntimeError  #unfinished, loop, not DAG
    #status = 0, unvisited
    status[v] = 1
    prerequisites = dependencies[v]
    pre_max = 0
    for node in prerequisites: pre_max = max(pre_max,DFS(node, dependencies))
    
    order[v] = pre_max+1
    status[v] = 2
    return order[v]
```
# Dijkstra
keep a priority q to store the closest vertex => explore
while pq:
    v1 = pq.pop_min; S.add(v1)
    for (v1,v2) in E:
        try to relax(v1,v2)
    pq.update_key(v2)

Ti: time to insert into PQ
Te: time to extract min key from PQ
Td: time to decrease key for PQ
O(|V|Ti + |V|Te + |E|Td)

heap: O((V+E)logV)
Fibonacci: O(VlogV + E)
# Bellman Ford
Idea:
1) initialize distance estimates
2) relax every edge V - 1 times

for k in range (V-1):
    for u in range(V):
        for v in adj[u]:
            try_to_relax(Adj, w, d, parent, u, v)

#if still relaxable, negative cycles
for u in range(V):
    for v in adj[u]:
        if d[v] > d[u] + w(u,v): raise Expeption("Negative cycle")
    
# Jhonson
The idea is to run Dijstra on every vertex: need to satisfy non-negative
SUPERNODE, run dijstra on supernode, h(u)
w'(u,v) = w(u,v) + h(u) - h(v)