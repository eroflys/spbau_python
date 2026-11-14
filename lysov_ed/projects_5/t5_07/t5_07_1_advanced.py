f = input()
s = input()
l = int(input())

print(len([
    (f[i:i + l], s[j:j + l])
    for i in range(len(f) - l + 1)
    for j in range(len(s) - l + 1)
    if f[i:i + l] == s[j:j + l]]))
