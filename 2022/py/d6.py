# tests
# data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# data = "bvwbjplbgvbhsrlpgdmjqwftvncz" #: first marker after character 5
# data = "nppdvjthqldpwncqszvftbrmjlhg" #: first marker after character 6
# data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" #: first marker after character 10
# data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #11

def get_data_string(file_name):
    file = open(file_name, "r")
    text = file.readlines()
    text = text[0].strip()
    return text


# load data
data = get_data_string("file6.txt")

# task 1 
quadruples = [x for x in zip(data[::],data[1::],data[2::],data[3::])]
first_uniqe = [x for x in quadruples if len(set(x)) == len(x)][0]
print("uniqe 4 ", first_uniqe)
print("4 position, ",quadruples.index(first_uniqe) + 4)


# task 2
fourteen = [x for x in zip(data[::],data[1::],data[2::],data[3::],data[4::],data[5::],data[6::],data[7::],data[8::],data[9::],data[10::],data[11::],data[12::],data[13::])]
first_uniqe = [x for x in fourteen if len(set(x)) == len(x)][0]
print("uniqe 14", first_uniqe)
print("14 position ",fourteen.index(first_uniqe) + 14)


