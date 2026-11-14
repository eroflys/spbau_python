seq = input().split()
commands = input().split()
skipped = 0

for i in commands:
    if i[0] == '+':
        seq.append(i[1:])
    elif i[0] == '-':
        r = -1
        c = 0
        for j in seq:
            if j == i[1:]:
                r = c
                break
            c += 1
        if r != -1:
            seq.pop(r)
        else:
            skipped += 1

if len(seq) == 0:
    print('нет')
else:
    print(*seq)
print(skipped)
