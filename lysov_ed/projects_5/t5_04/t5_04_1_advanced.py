f = input().split()
s = input().split()

f_min = min(int(f[1]), int(f[2]))
f_max = max(int(f[1]), int(f[2]))
s_min = min(int(s[1]), int(s[2]))
s_max = max(int(s[1]), int(s[2]))

print(max(0, min(f_max, s_max) - max(f_min, s_min) + 1))
