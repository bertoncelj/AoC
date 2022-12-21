import sympy


monkey = {}

def read_input(input_file):
    file = open(input_file, "r")
    text = file.readlines()
    text = [a.rstrip('\n') for a in text]
    return text

def main():
    # buffer = read_input("file21.txt")
    input = """
root: pppw + sjmn\n
dbpl: 5\n
cczh: sllz + lgvd\n
zczc: 2\n
ptdq: humn - dvpt\n
dvpt: 3\n
lfqf: 4\n
humn: 5\n
ljgn: 2\n
sjmn: drzm * dbpl\n
sllz: 4\n
pppw: cczh / lfqf\n
lgvd: ljgn * ptdq\n
drzm: hmdt - zczc\n
hmdt: 32\n
"""
    input = input.split("\n")
    buffer = [a for a in input if a]
    print(buffer)
        


    x = sympy.Symbol('x')
    f = 3 + x
    f = f - 3 + x + x + x - 2
    print(f)
    


    xx = sympy.Eq(f,0)
    print(sympy.solve(xx))

    monkey["humn"] = sympy.Symbol("x")

    for call in buffer:
        print(call)
        print(monkey)
        name, expr = call.split(": ")
        if name == "humn":
            continue
        if expr.isnumeric():
            monkey[name] = int(expr)
            print(sympy.solve(xx))
        else:
            left, op, right = expr.split()
            if left in monkey and right in monkey:
                if name == "root":
                    xx = sympy.Eq(monkey[left],monkey[right])
                    print(sympy.solve(xx))
                    break

                if op == "+":
                    monkey[name] = monkey[left] + monkey[right]
                elif op == "-":
                    monkey[name] = monkey[left] - monkey[right]
                elif op == "*":
                    monkey[name] = monkey[left] * monkey[right]
                elif op == "/":
                    monkey[name] = monkey[left] / monkey[right]
            else:
                buffer.append(call)
         

if "__main__" == __name__:
    main()
