import json

jsonfile = open('E:/NodeVScode/09.python_data/EXData/data02WHO.json', encoding='utf-8').read()
data = json.loads(jsonfile)

for row in data:
    print(row)
