initial = [2,5,2,3,5,3,5,5,4,2,1,5,5,5,5,1,2,5,1,1,1,1,1,5,5,1,5,4,3,3,1,2,4,2,4,5,4,5,5,5,4,4,1,3,5,1,2,2,4,2,1,1,2,1,1,4,2,1,2,1,2,1,3,3,3,5,1,1,1,3,4,4,1,3,1,5,5,1,5,3,1,5,2,2,2,2,1,1,1,1,3,3,3,1,4,3,5,3,5,5,1,4,4,2,5,1,5,5,4,5,5,1,5,4,4,1,3,4,1,2,3,2,5,1,3,1,5,5,2,2,2,1,3,3,1,1,1,4,2,5,1,2,4,4,2,5,1,1,3,5,4,2,1,2,5,4,1,5,5,2,4,3,5,2,4,1,4,3,5,5,3,1,5,1,3,5,1,1,1,4,2,4,4,1,1,1,1,1,3,4,5,2,3,4,5,1,4,1,2,3,4,2,1,4,4,2,1,5,3,4,1,1,2,2,1,5,5,2,5,1,4,4,2,1,3,1,5,5,1,4,2,2,1,1,1,5,1,3,4,1,3,3,5,3,5,5,3,1,4,4,1,1,1,3,3,2,3,1,1,1,5,4,2,5,3,5,4,4,5,2,3,2,5,2,1,1,1,2,1,5,3,5,1,4,1,2,1,5,3,5,2,1,3,1,2,4,5,3,4,3]

demo = [3,4,3,1,2]

#long way, do not work over 80 days plus
def req(lvl, ls, z_c_p):
    # print("in:", lvl, ls, z_c_p)

    if lvl == 0:
        return ls

    z_c = 0
    for n, el in enumerate(ls):
        if el - 1 == -1:
            ls[n] = 6
        elif el - 1 == 0:
            ls[n] = el - 1
            z_c = z_c + 1 
        else:
            ls[n] = el - 1

    for _ in range(z_c_p):
        ls.append(8)

    # print(ls)
    return req(lvl-1, ls, z_c)

def unlimited(lvl, ls, z_c_p):
    print(lvl)

    if lvl == 0:
        return ls

    z_c = 0
    for n, el in enumerate(ls):
        if el - 1 == -1:
            ls[n] = 6
        elif el - 1 == 0:
            ls[n] = el - 1
            z_c = z_c + 1 
        else:
            ls[n] = el - 1

    for _ in range(z_c_p):
        ls.append(8)

    # print(ls)
    return unlimited(lvl-1, ls, z_c)


#faster algo to get number of fishes over period of days
def fill_arr(ls):
    a =  [0,0,0,0,0,0,0,0,0]
    for elm in ls:
        a[elm] = a[elm] + 1
    return a
    

def next_day(ls):
    mle = ls[0]
    for n in range(0,6):
        ls[n] = ls[n+1] 
    ls[6] = mle
    ls[6] = ls[7] + ls[6]
    ls[7] = ls[8]
    ls[8] = mle

    return ls


#fill days
days = 256
fish = fill_arr(initial)
print("start", fish)
for _ in range(days):
    fish = next_day(fish)

print("end: ", fish,"sum:", sum(fish))






