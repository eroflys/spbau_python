f = float(input())
s = float(input())
t = float(input())

if (f >= s and f <= t) or (f >= t and f <= s):
    print(f)
elif (s >= f and s <= t) or (s >= t and s <= f):
    print(s)
else:
    print(t)
