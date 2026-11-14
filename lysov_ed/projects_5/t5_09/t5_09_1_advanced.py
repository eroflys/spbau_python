seq = input().split()
for i in zip(*seq):
    let_count = [i.count(j) for j in 'ACGT']
    max_am = 0
    max_am_count = 0
    max_am_pos = -1
    for j, am in enumerate(let_count):
        if am > max_am:
            max_am = am
            max_am_count = 1
            max_am_pos = j
        elif am == max_am:
            max_am_count += 1
    if max_am == 0:
        print('-', end='')
    elif max_am_count != 1:
        print('N', end='')
    else:
        print('ACGT'[max_am_pos], end='')
