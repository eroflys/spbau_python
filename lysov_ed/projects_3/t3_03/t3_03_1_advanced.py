seq = input()
threshold = float(input())

if len(seq) == 0:
    print(False)
else:
    print(100 * (seq.count('G') + seq.count('C')) / len(seq) > threshold)
