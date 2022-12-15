head = [0,0]
prev_head = [0,0]
tail = [0,0]
trace_tail = []
commands_input = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1","L 5", "R 2"]


def get_data(file_name):
    with open(file_name) as f:
        command_lines = list(map(str.rstrip,f))
    return command_lines

def move(direction, pos):
    x,y = pos
    if direction == "R":
        pos = [x+1,y]
    elif direction == "L":
        pos = [x-1,y]
    elif direction == "U":
        pos = [x,y+1]
    elif direction == "D":
        pos = [x,y-1]
    return pos

def walk(direction, steps):
    global head,prev_head, tail
    for step in range(steps):
        head = move(direction, head)
        tail = drag_tail(direction, tail, head,prev_head)

        if not tail in trace_tail:
            trace_tail.append(tail)
        prev_head = head


def drag_tail(direction, tail, head,prev):
    x_h,y_h = head
    x_t,y_t = tail

    rr = lambda x,y: x-y > 1 or x-y < -1

    if rr(x_h, x_t) or rr(y_h,y_t):
         tail = prev 
    return tail

        

commands_input = get_data("file9.txt")
t = lambda s: (s[0], int(s[2:]))
commands_input = list(map(t,commands_input))

for command in commands_input:
    walk(*command)
    print(head)
    print(tail)
    print()

print("---")
print(head)
print(tail)
print(len(trace_tail))
