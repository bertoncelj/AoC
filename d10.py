# ll = ["(",")",")","(",")","(",")",")","("]
# ll = ["(","{","}","{", "}",")"]
ll = list("{([(<{}[<>[]}>{[]{[(<()>")



def foo(ll, open):
    if len(ll) == 0:
        return True if len(open) == 0 else False

    print(ll, open)
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
        return get_num(check)

def get_num(character):
    nums = [3,57,1197,25137]
    orig = [")","]","}",">"]

    for n,_ in enumerate(nums):
        if character == orig[n]:
            return nums[n]

error = foo(ll,[])
print(error)






