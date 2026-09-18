with open("rosalind-datasets/rosalind_revc.txt", "r") as file:
    dna = file.read().strip()

dna_reverse = dna[::-1]

result = ""
for base in dna_reverse:
    if base == "A":
        result += "T"
    elif base == "T":
        result += "A"
    elif base == "C":
        result += "G"
    else:
        result += "C"

print(result)