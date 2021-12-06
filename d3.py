import numpy as np

def bin_to_int(list_bin):
    return int("".join(list(map(str, list_bin))),2)

file = open("binary_report.txt", "r")
lines = file.readlines()

bin_str = list(map(lambda s: list(s.strip()), lines))
bin = [list(map(int,a)) for a in bin_str]

#numpy matrix and transpose
a = np.array(bin).transpose()

#display matrix and shape 
print(a)
print(a.shape)

sum_rows = np.sum(a,axis=1)
gamma = list(map(lambda x: 1 if x > 500 else 0, list(sum_rows)))
print("gamma :",  gamma)

epsilon = list(map(lambda x: 0 if x == 1 else 1, list(gamma)))
print("epsilon", epsilon)

#task part one
#display gamma*epsion
num_gamma =   bin_to_int(gamma)
num_epsilon = bin_to_int(epsilon)
print("mul gamma*epsion = ", num_gamma*num_epsilon)



