cf = float(input('请输入摄氏度：'))
fc = cf * 1.8 + 32
print('%.2f摄氏度 = %.2f华氏度' % (cf, fc))
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))