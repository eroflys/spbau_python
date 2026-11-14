seq = input()
marks = input().split()
border = int(input())

last = -1
for i, b in enumerate(marks):
    if int(b) >= 20:
        last = i

if last == -1:
    print('пусто')
    print(len(seq))
else:
    print(seq[:last + 1])
    print(len(marks) - last - 1)
