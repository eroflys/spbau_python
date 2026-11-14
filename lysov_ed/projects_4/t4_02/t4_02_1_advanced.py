seq = input()
f = int(input())

for i in range(len(seq) - (len(seq) - f + 1) % 3, 2, -3):
    print(seq[i - 3:i])

if len(seq) - (len(seq) - f + 1) % 3 <= 2:
    print('NO')
