

class Parser():
    candidates = {
            "two":[(1)],
            "three":[(7)],
            "four":[(4)],
            "five":[(2,5,3)],
            "six":[(0,6,9)],
            "seven":[(8)],
        }

    segment = {
            "top": None,
            "top_left": None,
            "top_right": None,
            "middle": None,
            "bottom_left": None,
            "bottom_right": None,
            "bottom": None,
        }

    numbers_def = {
        "0":     ["top", "top_left", "top_right", "bottom_left", "bottom_right", "bottom"],
        "1":      ["top_right","bottom_right"],
        "2":      ["top", "top_right","middle", "bottom_left",  "bottom"],
        "3":    ["top", "top_right","middle",  "bottom_right", "bottom"],
        "4":     ["top_left", "top_right", "middle",  "bottom_right"],
        "5":     ["top", "top_left", "middle", "bottom_right", "bottom"],
        "6":      ["top", "top_left", "middle", "bottom_left", "bottom_right", "bottom"],
        "7":    ["top", "top_right", "bottom_right"],
        "8":    ["top", "top_left", "top_right", "middle", "bottom_left", "bottom_right", "bottom"],
        "9":     ["top", "top_left", "top_right", "middle", "bottom_right", "bottom"],
    }

    def __init__(self):
        pass

    def full_reset(self):

        candidates = {
            "two":[(1)],
            "three":[(7)],
            "four":[(4)],
            "five":[(2,5,3)],
            "six":[(0,6,9)],
            "seven":[(8)],
        }


        segment = {
            "top": None,
            "top_left": None,
            "top_right": None,
            "middle": None,
            "bottom_left": None,
            "bottom_right": None,
            "bottom": None,
            }
        self.candidates = candidates
        self.segment = segment


    def decript(self,decript_cipher, rez_cipher) :
        self.fill_candidates(decript_cipher)
        self.decipher()

        plain_num = ""
        for cipher in rez_cipher:
            plain_num = plain_num + self.word_to_num(cipher)
        self.full_reset()
        return plain_num

    def create_num_str(self,list_segment):
        rtn_str = ""
        for seg in list_segment:
            rtn_str = rtn_str + self.segment[seg]
        rtn_str = "".join(sorted(rtn_str))
        return rtn_str

    def word_to_num(self, word):
        word =  "".join(sorted(word))
        for key, value in self.numbers_def.items():
            if word == self.create_num_str(value):
                break
        return key

    def get_diff(self, str1, str2):
        diff = ""
        find_big_small = lambda a,b: (a,b) if len(a) > len(b) else (b,a) 
        bigger, smaller = find_big_small(str1,str2)
        for e in bigger:
            if not e in smaller:
                diff = diff + e
        return diff

    def print_dict(self, dd):
        for key, value in dd.items():
            print(key, ":", value)

    def used_letters(self):
        fin_str = ""
        for keys, value in self.segment.items():
            if value != None:
                fin_str = fin_str + str(value)
        return fin_str

    def find_same(self,words):
        for letter in words[0]:
            if letter in words[1] and letter in words[2] and not letter in self.segment["top"] and letter in words[3]:
                self.segment["middle"] = letter

        for letter in words[0]:
            if letter in words[1] and letter in words[2] and not letter in self.segment["top"] and not letter in self.segment["middle"]:
                self.segment["bottom"] = letter

    def get_four(self):
        str_one = self.candidates["two"][1]

        for candidate in self.candidates["four"][1:]:
            for letter in candidate:
                if not letter in str_one and not letter in [self.segment["middle"]]:
                    self.segment["top_left"] = letter

    def get_restOfThem(self):
        #get top right
        str_one = self.candidates["two"][1]
        used =  self.used_letters()
        for candidate in self.candidates["five"][1:]:
            can = candidate
            for letter in candidate:
                if letter in list(used):
                    can = can.replace(letter, '')
            if len(can) == 1:
                self.segment["bottom_right"] = can

        str_one = self.candidates["two"][1]
        bottom_right = str_one.replace(self.segment["bottom_right"],"")

        #get bottom right
        self.segment["top_right"] = bottom_right

        #get bottom_left
        last = "abcdefg"
        used = self.used_letters()
        for posible in used:
            last = last.replace(posible, "") 

        self.segment["bottom_left"] = last
        return None

    def decipher(self):
        str_one     = self.candidates["two"][1]
        str_seven   = self.candidates["three"][1]
        self.segment["top"] = self.get_diff(str_one, str_seven)
        str_can1 = self.candidates["five"][1]
        str_can2 = self.candidates["five"][2]
        str_can3 = self.candidates["five"][3]
        str_can4 = self.candidates["four"][1]

        self.find_same((str_can1, str_can2, str_can3, str_can4))
        self.get_four()
        self.get_restOfThem()

    def fill_candidates(self, cand):
        for word in cand:
            if len(word) == 2:
                self.candidates["two"].append(word)
            elif len(word) == 3:
                self.candidates["three"].append(word)
            elif len(word) == 4:
                self.candidates["four"].append(word)
            elif len(word) == 5:
                self.candidates["five"].append(word)
            elif len(word) == 6:
                self.candidates["six"].append(word)
            elif len(word) == 7:
                self.candidates["seven"].append(word)
            else:
                raise "Error"

file = open("digital_nums.txt", "r")
lines = file.readlines()
cipher_nums = list(map(lambda a:a.strip().split(), lines))

decript_cipher = list(map(lambda a:a[:10],cipher_nums ))
rez_cipher = list(map(lambda a:a[-4:], cipher_nums))

parse = Parser()
sum_ciphers = []

for next_cipher in range(len(decript_cipher)):
    p = parse.decript(decript_cipher[next_cipher], rez_cipher[next_cipher])
    sum_ciphers.append(int(p))
# print(sum_ciphers)
print(sum(sum_ciphers))


