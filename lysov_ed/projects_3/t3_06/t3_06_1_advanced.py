signal = float(input())
background = input()

if background == '':
    background = 0.05
else:
    background = float(background)

print(round(signal - background, 3))
