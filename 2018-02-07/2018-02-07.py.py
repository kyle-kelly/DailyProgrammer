# Python 3.6
# O(n) solution
from sys import stdin

# Read in data
length = int(stdin.readline())
seq = list(map(int, stdin.readline().split())) # thanks SO

# Initialize
tot_sum = sum(seq)
l_sum = 0
r_sum = tot_sum
idxs = []

# Iterate
for idx in range(length):
	if idx-1 >= 0:
		l_sum = l_sum + seq[idx-1]
	r_sum = r_sum - seq[idx]
	if l_sum == r_sum:
		idxs.append(idx)

print(" ".join(str(x) for x in idxs))