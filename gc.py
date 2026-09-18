sequence = {}
current_id = ""

while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.strip()
    if line.startswith(">"):
        current_id = line[1:]
        sequence[current_id] = ""
    else:
        sequence[current_id] += line

#print(sequence)

count_GC = 0
for base in sequence:
    if base == "G" or base == "C":
        count_GC += 1

print((count_GC/len(sequence)) * 100)