seq = input().split()

seq.sort(key=len)

if len(seq) % 2 == 1:
    print(len(seq[(len(seq) - 1) // 2]))
else:
    print((len(seq[len(seq) // 2]) + len(seq[len(seq) // 2 - 1])) / 2)
