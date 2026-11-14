start = int(input())
end = int(input())
sign = input()
p = int(input())

if sign == '-':
    print(end - p + 1)
else:
    print(p - start + 1)
