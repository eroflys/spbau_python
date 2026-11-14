seq = input()
k = int(input())

kmer = ''
am = 0
for i in range(len(seq) - k + 1):
    cur_kmer = seq[i:i+k]
    cur_am = 1
    for j in range(i + 1, len(seq) - k + 1):
        if cur_kmer == seq[j:j+k]:
            cur_am += 1
    if cur_am > am:
        am = cur_am
        kmer = cur_kmer

print(kmer, am)
