
# forest = [[3,0,3,7,3],
#           [2,5,5,1,2],
#           [6,5,3,3,2],
#           [3,3,5,4,9],
#           [3,5,3,9,0],
#          ]

forest = []

def get_forest_trees(file_name):
    with open(file_name) as f:
        tree_lines = map(str.rstrip,f)
        for trees in tree_lines:
            forest.append(list(map(lambda x: int(x),list(trees))))

def neighbors(row,col):
    check = lambda row,col: forest[row][col] if col >= 0 and row >= 0 and col < len(forest[0]) and row < len(forest) else -1
    left = lambda row,col: [check(row,i-1) for i in range(col,-1,-1)]
    right = lambda row,col: [check(row,i+1) for i in range(col,len(forest))]
    top = lambda row,col: [check(i-1,col) for i in range(row,-1,-1)]
    bottom = lambda row,col: [check(i+1,col) for i in range(row,len(forest))]
    return (top(row,col),bottom(row,col),left(row,col),right(row,col))

def any_obstractions(tree_height, neighbor_trees):
    return 1 if max(neighbor_trees) < tree_height else 0

def visiable_tree(row,col):
    for n in neighbors(row,col):
        if any_obstractions(forest[row][col],n):
            return 1
    return 0

def count_visiable_trees(n=4, ll=[2,3,4,-1]):
    for l in ll:
        print(l)

def main():
    get_forest_trees("file8.txt")
    visiable_trees = [ visiable_tree(row,col) for row in range(len(forest)) for col in range(len(forest[0]))]
    print("task1", sum(visiable_trees))

if __name__ == "__main__":
    main()
