file = open("digital_nums.txt", "r")
lines = file.readlines()

cipher_nums = list(map(lambda a:a.strip().split(), lines))
cipher_nums = list(map(lambda a:a[-4:], cipher_nums))

l_1478 = [2,3,4,7]
fin = 0
for cip in cipher_nums:
    fin = fin + sum(list(map(lambda a: 1 if len(a) in l_1478 else 0, cip)))
print(fin)


