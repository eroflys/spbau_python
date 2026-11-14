seq = input()

gc = 0
am = 0

for i in seq:
    if i == 'N':
        continue
    if i in ('G', 'C', 'S'):
        gc += 1
    if i in ('R', 'Y', 'K', 'M'):
        gc += 0.5
    am += 1

if am == 0:
    print(0.0)
else:
    print(round((gc / am) * 100, 1))
