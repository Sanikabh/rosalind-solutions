sequence = {}
current_id = ""

# Reading FASTA file format
with open("rosalind-datasets/rosalind_orf.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequence[current_id] = ""
        else:
            sequence[current_id] += line

codon_table = {
    'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
    'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'TAT':'Y', 'TAC':'Y', 'TAA':'Stop', 'TAG':'Stop',
    'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'TGT':'C', 'TGC':'C', 'TGA':'Stop', 'TGG':'W',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

seq = sequence[current_id] # store sequences in a separate variable

# Reverse complement
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
rev_comp = ""
for base in seq[::-1]:
    rev_comp += complement[base]

# define reading frame: scan one strand for every ORF
def find_proteins(s):
    found = set()
    for i in range(len(s) - 2):
        codon = s[i:i+3]
        if codon_table.get(codon) == "M":
            protein = ""
            for j in range(i, len(s), 3):
                c = s[j:j+3]
                aa = codon_table.get(c)
                if aa is None: # ran off the end, incomplete codon left over
                    break
                if aa == "Stop":
                    found.add(protein)
                    break
                protein += aa
    return found

proteins = set()
proteins |= find_proteins(seq) # 3 forward frames
proteins |= find_proteins(rev_comp) # 3 reverse complement frames

for p in proteins:
    print(p)