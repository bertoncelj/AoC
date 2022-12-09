from functools import reduce

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

def visiable_tree(row,col):
    for neighbor_trees in neighbors(row,col):
        if max(neighbor_trees) < forest[row][col]:
            return 1
    return 0

def range_view(row,col):
    ll = []
    for tree_range in neighbors(row,col):
        count = 0
        for tree in tree_range:
            if tree != -1:
                count += 1
                if forest[row][col] <= tree:
                    break
            else:
                break
        ll.append(count)
    return reduce((lambda x, y: x * y), ll)

def main():

    get_forest_trees("file8.txt")
    visiable_trees = [visiable_tree(row,col) for row in range(len(forest)) for col in range(len(forest[0]))]
    print("part1:", sum(visiable_trees))

    best_tree = [range_view(row,col) for row in range(len(forest)) for col in range(len(forest[0]))]
    print("part2:", max(best_tree))


if __name__ == "__main__":
    main()
