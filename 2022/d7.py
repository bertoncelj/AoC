free = 30000000
max_disk_space = 70000000

class DirTree:
    def __init__(self):
        self.parent = None 
        self.subdirs = []
        self.files_size = 0
        self.dir_size = 0

def get_filesystem(file_name):
    with open(file_name) as f:
        command_lines = list(map(str.rstrip,f))
    return command_lines

def parse_commands_history(file_system):
    get_num = lambda x: x[0] if len(x) == 2 else x[-1]

    filter_command = lambda command: 0 <= command.rfind("$ cd") or command[0].isdigit()
    return [ get_num(x.split(" ")) for x in filter(filter_command,file_system)]

def move_to_root(dir_p):
    while(dir_p.parent != None):
        dir_p = dir_p.parent
    return dir_p
    
def crate_directory_tree(dir_p,command_history):
    for command in command_history:
        if command.isdigit():
            dir_p.files_size += int(command)
        elif command != "..":
            dir_p.subdirs.append(DirTree())
            dir_p.subdirs[-1].parent = dir_p
            dir_p = dir_p.subdirs[-1]
        else:
            dir_p = dir_p.parent

    return move_to_root(dir_p)

def get_used_disk_size(dir_p):
    if dir_p.subdirs == []:
        dir_p.dir_size = dir_p.files_size
        return dir_p.files_size

    for subdir in dir_p.subdirs:
        dir_p.dir_size += get_used_disk_size(subdir) 

    dir_p.dir_size += dir_p.files_size
    return dir_p.dir_size

def sum_dirs_100000(dir_p,acc=0):

    for subdir in dir_p.subdirs:
        acc += sum_dirs_100000(subdir) 

    if dir_p.dir_size <= 100000:
        acc += dir_p.dir_size

    return acc 

def get_list_totals_directories(dir_p,ll=[]):

    for subdir in dir_p.subdirs:
        get_list_totals_directories(subdir,ll)

    ll.append(dir_p.dir_size)
    return ll

def delete_samllest(dir_p, used ):
    need_to_free = free - (max_disk_space - used)

    list_totals = get_list_totals_directories(dir_p)
    list_totals.sort()
    for candidate in list_totals:
        if candidate > need_to_free:
            return candidate
def main():

    file_system = get_filesystem("file7.txt")
    command_history = parse_commands_history(file_system)

    # create directory tree
    root_dir = DirTree()
    root_dir = crate_directory_tree(root_dir,command_history[1:])
    used_disk =  get_used_disk_size(root_dir)

    print("used disk", used_disk)
    print("sum_10000:", sum_dirs_100000(root_dir))
    print(delete_samllest(root_dir, used_disk))

if __name__ == "__main__":
    main()
