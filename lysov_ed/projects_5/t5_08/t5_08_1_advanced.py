n = int(input())

ids = []
seqs = []

for i in range(n):
    ids.append(input()[1:])
    seq = input()
    seqs.append([seq.count(j) for j in 'ACGT'])

avg_vec = []
for i in zip(*seqs):
    avg_vec.append(round(sum(i) / len(i), 2))

print(*avg_vec)

min_diff = -1
min_diff_pos = -1
for i, row in enumerate(seqs):
    diff = sum([abs(avg_vec[j] - row[j]) for j in range(4)])
    if min_diff == -1:
        min_diff = diff
        min_diff_pos = i
    elif min_diff > diff:
        min_diff = diff
        min_diff_pos = i

print(ids[min_diff_pos])
