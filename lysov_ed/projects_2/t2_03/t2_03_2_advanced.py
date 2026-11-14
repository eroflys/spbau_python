seq = input()
i = int(input())
j = int(input())

print(seq[:j] + seq[i - 1:j] + seq[j:])
