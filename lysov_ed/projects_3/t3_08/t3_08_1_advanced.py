n = input()
if len(n) != 3:
    print('неверная длина')
elif n[0] > 'H' or n[0] < 'A':
    print('неверный ряд')
elif (n[1] < '0' or n[1] > '1' or n[2] < '0' or
        n[2] > '9' or int(n[1:]) > 12 or int(n[1:]) < 1):
    print('неверный столбец')
else:
    print((ord(n[0]) - ord('A')) * 12 + int(n[1:]))
