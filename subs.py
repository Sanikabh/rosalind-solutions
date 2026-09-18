with open('rosalind-datasets/rosalind_subs.txt', "r") as file:
    s = file.readline().strip()
    t = file.readline().strip()

locations = []
for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        locations.append(i+1)

print(' '.join(str(x) for x in locations))