seq = input()

letter = seq[0]
ser_len = 0
res = ''

for i in seq:
    if i == letter:
        ser_len += 1
    else:
        res += letter + str(ser_len)
        letter = i
        ser_len = 1

res += letter + str(ser_len)
print(res)
