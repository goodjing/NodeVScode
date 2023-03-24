import pprint
import xlrd

book = xlrd.open_workbook('E:/NodeVScode/09.python_data/EXData/data04SOWC.xlsx')
sheet = book.sheet_by_name('Table 9')

count = 0
data = {}  # 添加一个字典

for i in range(14, sheet.nrows):
    row = sheet.row_values(i)  # 遍历每一行
    country = row[1]  # 取每一行第一个值
    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }
    if country == 'Zimbabwe':
        break  # 国家名字是'Zimbabwe'时退出循环

pprint.pprint(data)
