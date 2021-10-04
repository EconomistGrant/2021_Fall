```python
def two_lines(list_of_points):
    n = len(list_of_lines)
    count = {}
    for i in range(n):
        xi = list_of_points[i][0]
        yi = list_of_points[i][1]
        for j in range(n):
            xj = list_of_points[j][0]
            yj = list_of_points[j][1]
            if xi == xj:
                count[(np.nan,xi)] = count.get((np.nan,xi),0) + 1
            else:
                k = (yj-yi) / (xj-xi)
                b = yi - k * xi
                count[(k,b)] = count.get((k,b),0) + 1 
    
    sorted_count = sorted(count.items(),key =lambda x: x[1], reverse = True)
    max_count = sorted_count[0][1]
    if max_count < (n/2)*(n/2-1):
        return False
    max_line = sorted_count[0][0]
    rest_list_of_points = []
    if max_line[0]!=np.nan:
        k = max_line[0]
        b = max_line[1]
        for i in range(n):
            xi = list_of_points[i][0]
            yi = list_of_points[i][1]          
            if abs(yi - b + k * xi) > 1e-5:
                rest_list_of_points.append((xi,yi))
    else if 
    
    
    
    