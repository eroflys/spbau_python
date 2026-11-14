L = int(input())

cur = 0
res = 1
is_any_frag = False
while True:
    new = input()
    if new == 'done':
        break
    is_any_frag = True
    new = int(new)
    if cur + new <= L:
        cur += new
    else:
        cur = new
        res += 1

if is_any_frag:
    print(res)
else:
    print(0)
