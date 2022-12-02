def get_calories(input_file):
    file = open(input_file, "r")
    text = file.read()[:-1]
    la = text.split("\n\n")
    ll =  list(map(lambda x: x.split("\n"),la))
    return ll

calories = get_calories("calories.txt")
calories = [list(map(lambda x: int(x),cal))for cal in calories]
max_list = [sum(cal) for cal in calories]
max_list.sort()
print(sum(max_list[-3:]))
