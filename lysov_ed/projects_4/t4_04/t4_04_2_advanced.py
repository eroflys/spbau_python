m = input()

counter = 0
res = 1
if_res = False
while True:
    new = input()
    if new == 'done':
        break
    if if_res:
        continue
    if m in new and 'N' not in new:
        res = counter
        if_res = True
    counter += 1

if if_res:
    print(res + 1)
else:
    print(0)
