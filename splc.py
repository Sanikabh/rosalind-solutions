# RNA splicing
sequence = {}
current_id = ""
first_id = None # capturing first_id

while True:
    try:
        line = input()
    except EOFError:
        break
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

