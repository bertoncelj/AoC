from functools import reduce

get_nums = lambda line: [(n,e) for n,e, in enumerate(line) if e in "0123456789" ]
numbers_positions = lambda x,y: numbers(get_nums(x),0,y)

def numbers(oldl,n,newl):
    if oldl == []:
        return []

    position, charater = oldl[0][0],oldl[0][1]

    if (n < position or position == 0):
        newl.append([position, position,""])
        n = position
     
    newl[-1][2] += charater
    newl[-1][1] =  position+1
    
    return newl + numbers(oldl[1:],n+1,newl) if n == 0 else numbers(oldl[1:],n+1,newl)


board = list(open('data.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}
for r, row in enumerate(board):
    newl = []
    numbers_positions(row,newl)
    for n in newl:

        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n[0]-1, n[1]+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n[2]))

print("part 1:", sum(sum(p)    for p in chars.values()))
print("part 2:", sum(reduce(lambda x,y: x*y, p) for p in chars.values() if len(p)==2))
