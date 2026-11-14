seq = input()

if len(seq) == 0:
    print('пустая')
elif (seq.count('A') + seq.count('C') + seq.count('G') + seq.count('T') +
        seq.count('N') + seq.count('a') + seq.count('c') + seq.count('g') +
        seq.count('t') + seq.count('n') != len(seq)):
    print('недопустимые символы')
elif seq.count('N') + seq.count('n') > len(seq) * 0.5:
    print('низкое качество')
elif (seq.count('a') + seq.count('c') + seq.count('g') +
        seq.count('t') + seq.count('n') == len(seq)):
    print('замаскирована')
else:
    print('OK')
