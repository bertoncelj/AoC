import sys
# recursion set limit over 2000
sys.setrecursionlimit(2300)


def find_end_depth(deep_log):
    return sum(list(map(lambda a,b: 1 if a < b else 0, 
                    deep_log[0:], deep_log[1:])))

def main():
#load file
    file = open("deeps.txt", "r")
    lines = file.readlines()
    deeps = list(map(lambda s: int(s.strip()), lines))


    max_deepth = sum(list(map(lambda a,b: 1 if a < b else 0, 
                            deeps[0:], deeps[1:])))

    sum_three_together = list(map(lambda x,y,z: x+y+z, 
                            deeps[0:], deeps[1:],deeps[2:]))


    max_sigle_depth = find_end_depth(deeps)
    max_sum_triplets_depth = find_end_depth(sum_three_together)

    print(max_sigle_depth)
    print(max_sum_triplets_depth)


if __name__ == "__main__":
    main()
