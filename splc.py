# RNA splicing
sequence = {}
current_id = ""
first_id = None # capturing first_id

with open("rosalind-datasets/rosalind_splc.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            sequence[current_id] = ""
            if first_id is None:
                first_id = current_id
        else:
            sequence[current_id] += line

main_seq = sequence[first_id]
#print(main_seq)

for key in sequence:
    if key == first_id:
        continue
    intron = sequence[key]
    main_seq = main_seq.replace(intron, "")
#print(main_seq)

rna_main_seq = main_seq.replace("T", "U")

proteins = []
codon_table = {
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}

for i in range(0, len(rna_main_seq), 3):
    codon = rna_main_seq[i:i+3]
    aa = codon_table[codon]
    if aa == "Stop":
        break
    proteins.append(aa)

print(''.join(proteins))