seq = input()
start_index = -1

for i in range(len(seq)):
    if seq[i:i+3] == 'ATG':
        start_index = i

res = 0
is_res_exist = False
if start_index != -1:
    for i in range(start_index, len(seq) - 2, 3):
        if seq[i:i+3] in ('TAA', 'TAG', 'TGA'):
            is_res_exist = True
            break
        res += 1

if is_res_exist:
    print(res)
else:
    print('NO')
