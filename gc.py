dna = input()

count_GC = 0

for base in dna:
    if base == "G" or base == "C":
        count_GC += 1

print((count_GC/len(dna)) * 100)