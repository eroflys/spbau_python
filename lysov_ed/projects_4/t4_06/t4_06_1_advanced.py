n = int(input())

f_m = 0
s_m = 0
for i in range(n):
    new = int(input())
    if new >= f_m:
        s_m = f_m
        f_m = new
    elif new > s_m:
        s_m = new

print(f_m, s_m)
