
def get_data(file_path):
    file = open(file_path, "r")
    lines = file.readlines()

    pos = []
    for line in lines:
        vents = list(line.strip().split("->" ))
        v = tuple([tuple(map(int,a.split(","))) for a in vents])
        pos.append(v)
    return pos

def get_points(pair_points):
    point1, point2 = pair_points
    x1, y1 = point1
    x2, y2 = point2
    return x1,y1,x2,y2

def check_linear(pair_points):
    x1,y1,x2,y2 = get_points(pair_points)
    if x1 == x2 or y1 == y2:
        # print("linear: p1:", (x1,y1) ,"p2:", (x2,y2))
        return True
    else:
        return False 

def point_to_str(x,y):
    return str(x)+","+str(y)

def add_points_list_in_diagram(points, dic_co):

    for point in points: 
        x, y = point
        p_str = point_to_str(x,y)

        if not p_str in dic_co:
            dic_co[p_str] = 1
        else:
            dic_co[p_str] = dic_co[p_str] + 1

def StB(a,b):
    return (a,b+1) if a <= b else (b,a+1)

def add_points(dic_co, linear_points):

    x1,y1,x2,y2 = get_points(linear_points)
    if x1 == x2:
       v = tuple([(x1, a) for a in range(*StB(y1,y2))])
       add_points_list_in_diagram(v, dic_co)
    elif y1 == y2:
       v = tuple([(a, y1) for a in range(*StB(x1,x2))])
       add_points_list_in_diagram(v, dic_co)
    else:
        print("ERROR")

def find_max_num_diagram(coordinate):
    val_f = 0
    for key in coordinate.keys():
        if coordinate[key] > val_f:
            val_f = coordinate[key]

    return val_f


def count_max_num_diagram(coordinate, max_num):
    count = 0
    for key in coordinate.keys():
        if coordinate[key] >= max_num:
            count = count + 1
    return count



data_vents = get_data("vents.txt")
coordinate= {}

for p in data_vents:
    if check_linear(p):
        add_points(coordinate, p)

# max_num = find_max_num_diagram(coordinate)
# print(max_num)
c_n = count_max_num_diagram(coordinate, 2)
print(c_n)


