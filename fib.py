# Rabbits and recurrence relations
with open("rosalind-datasets/rosalind_fib.txt", "r") as file:
    line = file.readline()

n, k = map(int, line.strip().split())

# track the two most recent months
two_months_ago = 1  # month 1
last_month = 1       # month 2

for month in range(3, n + 1):
    this_month = last_month + k * two_months_ago
    two_months_ago = last_month
    last_month = this_month

print(last_month)