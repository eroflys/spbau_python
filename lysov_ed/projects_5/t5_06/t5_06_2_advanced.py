n = int(input())
seqs = []

for i in range(n):
    seqs.append(input().split())
    seqs[-1].append((seqs[-1][1].count('C') +
                    seqs[-1][1].count('G')) / len(seqs[-1][1]))

print(*[i[0] for i in sorted(seqs, key=lambda x: (-x[2], x[0]))])
