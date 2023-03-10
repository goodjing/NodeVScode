import csv

f = open('E:/NodeVScode/09.python_data/EXData/data01WHO.csv')
readers = csv.reader(f)
readerdic = csv.DictReader(f)

# 输出每行内容为列表
# for row in readers:
#     print(row)

# 输出每行内容为字典
for row1 in readerdic:
    print(row1)
