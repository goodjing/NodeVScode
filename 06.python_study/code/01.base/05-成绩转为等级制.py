score = float(input('输入成绩：'))
if 90 <= score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 40:
    grade = 'D'
elif score >= 0:
    grade = 'E'
print('成绩对应等级为：', grade)
