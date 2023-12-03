number_table = (
    ("one","1"),
    ("two","2"),
    ("tw1","21"),
    ("three","3"),
    ("four","4"),
    ("five","5"),
    ("six","6"),
    ("seven","7"),
    ("seve9","79"),
    ("eight","8"),
    ("eigh2","82"),
    ("eigh3","83"),
    ("1ight","18"),
    ("3ight","38"),
    ("5ight","58"),
    ("nine","9"),
    ("7ine","79"),
)

def get_calibrations(input_file):
    file = open(input_file, "r")
    text = file.read()[:-1]
    return text.split("\n")

def get_numbers(text):
    list_num = [x for x in text if x.isdigit() ]
    print(list_num)
    return int(list_num[0] + list_num[-1]) if(list_num != []) else 0

def replace_words_with_numbers(statement):
    tmp = statement
    for number in number_table:
        tmp = tmp.replace(*number) 
    print(tmp)
    return tmp

final_day_1 = []
inputs = get_calibrations("calibrations.txt")
for text in inputs:
    final_day_1.append(get_numbers(text))

print("result of day1: ", sum(final_day_1))

final_day_2 = []
for text in inputs:
    print("in", text)
    final_day_2.append(get_numbers(replace_words_with_numbers(text)))

print("result of day2: ", sum(final_day_2))
