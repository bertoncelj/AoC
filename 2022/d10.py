test = """noop
addx 3
addx -5"""

cycle = 0
x = 1
si = False

# open the data file
file = open("file10.txt")
with open("file10.txt") as f:
    data = list(map(str.rstrip,f))

print(data)
check = list(range(20,220,20))
xx = [["noop"] if a == "noop" else ["noop",a] for a in data]
test = [item for sublist in xx for item in sublist]

for line in test:
    cycle += 1
    if "noop" == line:
        pass
    else:
        _, num = line.split()
        x += int(num)
    if check[0] == cycle:
        c = check.pop(0)
        print(c)
        print(x)
        print(c*x)

print("x:", x) 
print("cycle:", cycle) 

