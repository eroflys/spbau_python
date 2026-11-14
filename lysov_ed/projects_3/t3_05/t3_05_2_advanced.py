systolic = int(input())
diastolic = int(input())

if systolic < 120 and diastolic < 80:
    print('оптимальное')
elif systolic < 130 and diastolic < 85:
    print('нормальное')
elif systolic < 140 and diastolic < 90:
    print('высокое нормальное')
else:
    print('гипертензия')
