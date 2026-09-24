# RNA splicing
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

