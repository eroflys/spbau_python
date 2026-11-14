name = input().split()[0][1:]
seq = input()

print(name, len(seq), round(100 * (seq.count('g') + seq.count('c') + seq.count('G') + seq.count('C')) / len(seq), 1), round(100 * (seq[2::3].count('g') + seq[2::3].count('c') + seq[2::3].count('G') + seq[2::3].count('C')) / len(seq[2::3]), 1), sep='\t')
