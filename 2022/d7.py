class DirTree:
    def __init__(self,name=None):
        self.parent = None 
        self.subdirs = []
        self.name = name 
        self.files = []
        self.sum_total = 1

    def create_dir(self,name):
        self.subdirs.append(DirTree(name))

def goto_root(self):
    if self.parent != None:
        return goto_root(self.parent)


def print_dir(self, deep=0):
    print(" "*deep, self.name)
    deep += 1
    for a in self.subdirs:
        print_dir(a,deep) 
    return

def get_filesystem(file_name):
    with open(file_name) as f:
        command_lines = list(map(str.rstrip,f))
    return command_lines

def parse_dir_commands(file_system):
    filter_cd = filter(lambda command: 0 <= command.rfind("$ cd"),file_system)
    return list(filter_cd)

# root = DirTree("root")
# root.subdirs.append(DirTree("a"))
# root.subdirs.append(DirTree("b"))
# root.subdirs.append(DirTree("c"))
# root.subdirs[0].subdirs.append(DirTree("e"))
# root.subdirs[0].subdirs.append(DirTree("d"))
# root.subdirs[0].subdirs.append(DirTree("g"))
# root.subdirs[1].subdirs.append(DirTree("g"))
# root.subdirs[1].subdirs.append(DirTree("g"))
# ["cd root"]
# print_dir(root)

def print_node(self):
    print("parent: ", self.parent)
    print("subdirs: ", self.subdirs)
    print("name: ", self.name)

def crate_directory_tree(x,pp):
    for p in pp:
        print_node(x)
        print("")
        if p != "..":
            x.subdirs.append(DirTree(p))
            x.subdirs[-1].parent = x
            x = x.subdirs[-1]
        else:
            x = x.parent
    return move_to_root(x)

def move_to_root(x):
    while(x.parent != None):
        x = x.parent
    return x

def count_all_file_sizes(x,acc=0):
    for subdir in x.subdirs:
        acc += count_all_file_sizes(subdir,acc)
    acc += x.sum_total
    print("return")  
    print_node(x)
    print("acc", acc)
    print("")
    return acc  

file_system = (get_filesystem("file7.txt"))
pp = parse_dir_commands(file_system)
pp = [x.split(" ")[-1] for x in pp]
print(pp)

x = DirTree(pp[0])
root = x
x = crate_directory_tree(x,pp[1:])
print(count_all_file_sizes(x,0))






