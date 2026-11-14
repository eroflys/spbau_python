f = input()
s = input()

transition = 0
transversion = 0

for i in range(len(f)):
    if f[i] == 'N' or s[i] == 'N' or f[i] == s[i]:
        continue
    if (
        (f[i] == 'A' and s[i] == 'G') or
        (f[i] == 'G' and s[i] == 'A') or
        (f[i] == 'C' and s[i] == 'T') or
        (f[i] == 'T' and s[i] == 'C')
    ):
        transition += 1
    else:
        transversion += 1

if transversion != 0:
    print(round(transition / transversion, 2))
else:
    print('NA')
