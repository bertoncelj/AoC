def load_brackets(filename):
    file = open(filename, "r")
    lines = file.readlines()
    return list(map(lambda a:a.strip(), lines))

def get_num1(character):
    nums = [ 1,  2,  3,  4 ]
    orig = ["(","[","{","<"]

    for n,_ in enumerate(nums):
        if character == orig[n]:
            return nums[n]

def foo1(lll,score):
    if len(lll) == 0:
        return (True,score)
    
    score *= 5
    score += get_num1(lll.pop())
    return foo1(lll,score)


def foo(ll, open):
    if len(ll) == 0:
        print("last", open)
        if len(open) != 0:
            score = 0
            return foo1(open,score)

    # print(ll, open)
    check = ll.pop(0)
    if check in ["(","{","[","<"]:
        open.append(check)
        return foo(ll,open)

                  
    if len(open) > 0 and check == ")" and open[-1] == "(":
        open.pop()
        return foo(ll,open)

    elif len(open) > 0 and check == "}" and open[-1] == "{":
        open.pop()
        return foo(ll,open)

    elif len(open) > 0 and check == "]" and open[-1] == "[":
        open.pop()
        return foo(ll,open)

    elif len(open) > 0 and check == ">" and open[-1] == "<":
        open.pop()
        return foo(ll,open)

    else:
        print("Must have",open[-1], "not", check)
        return (False,0)

def get_num(character):
    nums = [1,57,1197,25137]
    orig = [")","]","}",">"]

    for n,_ in enumerate(nums):
        if character == orig[n]:
            return nums[n]


def get_close_bracket(character):
    open = ["(","[","{","<"]
    close = [")","]","}",">"]
    
    for n,_ in enumerate(open):
        if character == open[n]:
            return close[n]


list_brackets = load_brackets("bracket.txt")
autocomplete = []
for brackets in list_brackets:
    check,score = foo(list(brackets),[])
    if check == True:
        autocomplete.append(score)

autocomplete.sort()
print(autocomplete)
print(autocomplete[int(len(autocomplete)/2)])



