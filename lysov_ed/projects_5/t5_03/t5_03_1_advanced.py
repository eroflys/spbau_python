seq = input().split()
i = int(input())
j = int(input())

if i < j:
    res = [seq[i] for i in range(i - 1, j)]
else:
    res = [seq[i] for i in range(i - 1, j - 2, -1)]

print(*res)
