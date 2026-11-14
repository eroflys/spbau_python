f = input()
s = input()

if len(f) > len(s):
    z = zip(f[len(f) - len(s):], s)
elif len(f) < len(s):
    z = zip(f, s[len(s) - len(f):])
else:
    z = zip(f, s)

res = 0
for i in z:
    if i[0] != i[1]:
        res += 1

print(res)
