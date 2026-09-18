sequence = {}
current_id = ""

with open('rosalind-datasets/rosalind_gc.txt', "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequence[current_id] = ""
        else:
            sequence[current_id] += line

    #print(sequence)
    best_id = ""
    best_gc = 0

    for seq_id, seq in sequence.items():
        count_GC = 0
        for base in seq:
            if base == "G" or base == "C":
                count_GC += 1
        gc_content = (count_GC/len(seq)) * 100
        #print(gc_content)

        if gc_content > best_gc:
            best_gc = gc_content
            best_id = seq_id

    print(best_id, best_gc)