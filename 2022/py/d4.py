def get_elf_assignments(input_file):
    file = open(input_file, "r")
    text = file.readlines()
    text = [a.rstrip('\n') for a in text]
    text = [ t.split(",") for t in text]

    zip_id = lambda x: x.split("-")
    ii = lambda x: [int(n) for n in zip_id(x)]
    zip_pair = lambda first,secod: (ii(first), ii(secod))
    return [zip_pair(pair[0],pair[1]) for pair in text]

def contain_all(ids):
    c = 0
    for e, id in enumerate(ids):
        e1,e2 = id
        if e1[0] <= e2[0] and e1[1] >= e2[1]:
            c += 1
        elif e1[0] >= e2[0] and e1[1] <= e2[1]:
            c += 1
    return c

def overlap_any(ids):
    c = 0
    for e, id in enumerate(ids):
        e1,e2 = id

        if e1[1] >= e2[0] and e1[0] <= e2[1] :
            c += 1
    return c
    
    

elf_pairs_tasks = get_elf_assignments("file4.txt")
print("task1:", contain_all(elf_pairs_tasks))
print("task1:", overlap_any(elf_pairs_tasks))
