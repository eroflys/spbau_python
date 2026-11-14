n = int(input())

if n == 0:
    print(0)
else:
    res = ''
    while n > 0:
        res += str(n % 2)
        n //= 2
    for i in res[-1::-1]:
        print(i, end='')
