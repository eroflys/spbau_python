seq = input()

g = 0
c = 0
min_i = 0
min_i_am = 0

for i in range(len(seq)):
    if seq[i] == 'G':
        g += 1
    if seq[i] == 'C':
        c += 1
    if g - c < min_i_am:
        min_i = i + 1
        min_i_am = g - c

print(min_i)
