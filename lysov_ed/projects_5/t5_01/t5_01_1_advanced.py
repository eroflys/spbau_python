seq = input().split()
prev = []
dub = []

for i in seq:
    if i in prev:
        if i not in dub:
            dub.append(i)
    else:
        prev.append(i)

if len(dub) == 0:
    print('нет')
else:
    print(*dub)
