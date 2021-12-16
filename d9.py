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
    if t == None and r == None and b == None and l == None:
        print("Non existing")
        return None
    else:
        print("in:", x,y, "->",t,r,b,l)

matrix = fill_matrix("poligon.txt")
max_y = len(matrix)
max_x = len(matrix[0])

print("matrix", max_x, ",",max_y)
for m in matrix:
    print(m)

print(poligon(19,20))
print(poligon(2,2))
for a in range(len(matrix[0])):
    get_neighbours(0,a)



