with open("rosalind-datasets/rosalind_rna.txt", "r") as file:
    dna = file.read().strip()

print(dna.replace("T", "U"))