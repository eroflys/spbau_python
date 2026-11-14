threshold = float(input())
f = input()
s = input()
t = input()

if f != '' and float(f) > threshold:
    print(0)
elif s != '' and float(s) > threshold:
    print(1)
elif t != '' and float(t) > threshold:
    print(2)
else:
    print('нет сигнала')
