with open('rosalind-datasets/rosalind_hamm.txt', "r") as file:
    s = file.readline().strip()
    t = file.readline().strip()

count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count += 1
print(count)