with open('rosalind-datasets/rosalind_dna.txt', "r") as file:
    n = file.read().strip()
a = n.count("A")
c = n.count("C")
g = n.count("G")
t = n.count("T")

print(a, c, g, t)
