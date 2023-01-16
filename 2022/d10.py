test = """noop
addx 3
addx -5"""

cycle = 0
x = 1

# open the data file
file = open("file10.txt")
with open("file10.txt") as f:
    data = list(map(str.rstrip,f))

# check intervales
check = list(range(20,1000,40))

#insert noops before each addx
xx = [["noop"] if a == "noop" else ["noop",a] for a in data]
test = [item for sublist in xx for item in sublist]

signal = []
for line in test:
    cycle += 1

    if check[0] == cycle:
        c = check.pop(0)
        signal.append(c*x)

    if "noop" == line:
        pass
    else:
        _, num = line.split()
        x += int(num)

print(sum(signal))
