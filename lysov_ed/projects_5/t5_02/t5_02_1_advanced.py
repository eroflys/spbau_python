seq = input().split()
shift = int(input())
res = [''] * len(seq)

counter = 0
for i in seq:
    if counter + shift < len(seq) and counter + shift >= -len(seq):
        res[counter + shift] = i
    else:
        res[(counter + shift) % len(seq)] = i
    counter += 1

print(*res)
