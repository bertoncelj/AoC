his = []

def fill_matrix(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    bin = list(map(lambda s: list(s.strip()), lines))
    bin = [list(map(int,a)) for a in bin]
    m = []
    for line in bin:
        m.append(line)
    return m

def poligon(x,y):
    try:
        return matrix[y][x]
    except IndexError:
        return None

def get_top(x,y):
    y = y-1
    if y < 0:
        return None
    else:
        return poligon(x,y)

def get_left(x,y):
    x = x-1
    if x < 0:
        return None
    else:
        return poligon(x,y)

def get_bot(x,y):
    y = y + 1
    if len(matrix) < y:
        return None
    else:
        return poligon(x,y)

def get_right(x,y):
    x = x + 1
    if len(matrix[0]) < x:
        return None
    else:
        return poligon(x,y)
    
def get_neighbours(x,y):
    t = get_top(x,y)
    r = get_right(x,y)
    b = get_bot(x,y)
    l = get_left(x,y)

    return [t,r,b,l]

def minimum(elem, neighbours):
    neighbours = list(map(lambda x: 9 if x == None else x, neighbours))
    if all(elem < n for n in neighbours):
        return True 
    else:
        return False

def get_neigh_coords(x,y, n, elem):
    if elem == None:
        return (None, None)
    #top
    if n == 0:
        return (x,y-1) 
    #right
    elif n == 1:
        return (x+1,y) 
    #bottom
    elif n == 2:
        return (x,y+1) 
    #left
    elif n == 3:
        return (x-1,y) 

def rec(x, y):
    if x == None:
        return 0

    if matrix[y][x] == 9:
        return 0

    if (x,y) in his:
        return 0

    his.append((x,y))
    neigh = get_neighbours(x,y)

    x_0, y_0 = get_neigh_coords(x,y,0, neigh[0])
    x_1, y_1 = get_neigh_coords(x,y,1, neigh[1])
    x_2, y_2 = get_neigh_coords(x,y,2, neigh[2])
    x_3, y_3 = get_neigh_coords(x,y,3, neigh[3])

    
    return rec(x_0, y_0) + rec(x_1, y_1) + rec(x_2, y_2) + rec(x_3, y_3) + 1


matrix = fill_matrix("poligon.txt")
max_y = len(matrix)
max_x = len(matrix[0])

print("matrix", max_x, ",",max_y)

discoverd_minimums = []
for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        neigh = get_neighbours(x,y)
        elem = matrix[y][x]
        if minimum(elem, neigh):
            discoverd_minimums.append(rec(x,y))

discoverd_minimums.sort()
x,y,z = discoverd_minimums[-3:]
print("Resulut", x*y*z)










