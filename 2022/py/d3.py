# day 3

lower="a"
lower_alphabet = [(chr(ord(lower)+i)) for i in range(26)]

upper="A"
upper_alphabet = [(chr(ord(upper)+i)) for i in range(26)]
alphabet = lower_alphabet + upper_alphabet

def get_items_from_rucksacks(input_file):
    file = open(input_file, "r")
    text = file.readlines()
    text = [a.rstrip('\n') for a in text]
    return text



def split_string_half(s):
    return s[:len(s)//2], s[len(s)//2:]

def find_same_character(s1,s2):
    return list(set(s1)&set(s2))

def get_grupe_ch(s1,s2,s3):
    return list(set(s1)&set(s2)&set(s3))

def get_letter_number(letter):
    for pos,ch in  enumerate(alphabet):
        if ch == letter:
            return pos + 1


# part 1
items = get_items_from_rucksacks("file3.txt")
find_common_letter = list(map(lambda x:  find_same_character(*split_string_half(x))[0], items))
print("day3_part1: ", sum(map(lambda x: get_letter_number(x),find_common_letter)))

# part 2
items = get_items_from_rucksacks("file3.txt")
groupe_3 = list(zip(items[::3],items[1::3],items[2::3]))
find_common_letter = list(map(lambda x:  get_grupe_ch(*x)[0], groupe_3))
print("day3_part2: ", sum(map(lambda x: get_letter_number(x),find_common_letter)))
