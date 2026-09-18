with open('rosalind-datasets/rosalind_dna.txt', "r") as file:
    n = file.read().strip()

print(n.count("A"), n.count("C"), n.count("G"), n.count("T"))
