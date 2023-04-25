test = """noop
addx 3
addx -5"""


# open the data file
file = open("file10.txt")
with open("file10.txt") as f:
    input = list(map(str.rstrip,f))

# check intervales
check = list(range(20,1000,40))

#insert noops before each addx
xx = [["noop"] if a == "noop" else ["noop",a] for a in input]
data = [item for sublist in xx for item in sublist]

def signal_strength(data):
    cycle = 0
    x = 1
    signal = []
    for line in data:
        cycle += 1

        if check[0] == cycle:
            c = check.pop(0)
            signal.append(c*x)

        if "noop" == line:
            pass
        else:
            _, num = line.split()
            x += int(num)
    return sum(signal)

def draw_row(data):
    sprite = list(range(0,3))
    display = []
    x = 1 
    crt = 0 
    cycle = 1
    for line in data:
        if crt in sprite:
            display.append("#")
        else:
            display.append(".")

        if line != "noop":
            _, num = line.split()
            x += int(num)

        crt += 1
        cycle += 1
        sprite = list(range(x-1,x+2))
    print("".join(display))
    
def part2(data):
    for x in range(6):
        draw_row(data[x*40:(x+1)*40]) 

def part1(data):
    print(signal_strength(data))

    
part1(data)
part2(data)
