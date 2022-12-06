# stacks = [
#     ["Z", "N"],
#     ["M", "C","D"],
#     ["P"],
# ]
   
stacks = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

def get_inputs_stacks(input_file):
    file = open(input_file, "r")
    lines = file.readlines()
    for line in range(8):
        for n,crate in enumerate(lines[line][1::4]):
            if crate != " ":
                stacks[n] = [crate] + stacks[n]

def get_inputs_sequence(input_file):
    file = open(input_file, "r")
    lines = file.readlines()[10:]
    lines = list(map(lambda x: x.strip().split(" "),lines))
    return [ (int(ll[1]),int(ll[3]),int(ll[5])) for ll in lines]

def put_on_stack(stack_x, letter):
    return stacks[stack_x-1].append(letter)

def take_from_stack(stack_x, take=-1):
    return stacks[stack_x-1].pop(take)

def move_stack(move, move_from, move_to):
    # check valid moves
    if move > len(stacks[move_from-1]):
        raise Exception("to many moves")

    for move_counter in range(move):
        crate = take_from_stack(move_from)
        put_on_stack(move_to, crate)

def move_stack_9001(move, move_from, move_to):
    for move_counter in range(-move,0,1):
        crate = take_from_stack(move_from, move_counter)
        put_on_stack(move_to, crate)

def print_stacks():
    print("_"*5)
    for pos, stack in enumerate(stacks, start=1):
        print(pos, stack)
    print("_"*5)

def read_top_stacks():
    for stack in stacks:
        print(stack[-1])

def run_sequence(program_list,crane_model):
    # program_list = [(1,2,1),(3,1,3),(2,2,1),(1,1,2)]
    for execute in program_list:
        move, move_from, move_to = execute

        if crane_model == 9000:
            move_stack(move, move_from, move_to)
        else:
            move_stack_9001(move, move_from, move_to)


get_inputs_stacks("file5.txt")
program_sequence = get_inputs_sequence("file5.txt")

# run_sequence(program_sequence,90000)
# print("task1:") 
# read_top_stacks()

run_sequence(program_sequence,90001)
print("task2:")
read_top_stacks()
