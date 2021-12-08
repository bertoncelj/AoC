file = open("bingo_0.txt", "r")
lines = file.readlines()

bingo_numbers = list(map(int, lines[0].strip().split(",")))

def get_matrix(file_lines):
    all = []
    matrix = [] 
    for line in file_lines:
        if line == "\n":
            all.append(matrix)
            matrix = [] 
        else:
            line = list(map(int, 
                   line.strip().split()))
            matrix.append(line)
    all.append(matrix)
    return all

def check(rows, num):
    if num in rows:
        rows.remove(num)
    return rows
    

all = get_matrix(lines[2:])
print(bingo_numbers)
for num in bingo_numbers: 
    for row in all[0]:
        check(row, num)
        print(row)
    print("-"*10)

