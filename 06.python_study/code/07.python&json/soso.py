import json

py_data = {"name": "张三", "age": "24", "job": "法外狂徒"}

# 转换成json对象时，编码默认为Unicode，ensure_ascii=False 取消默认编码
with open('./练习文件/json.json', 'w', encoding='utf-8') as f:
    json.dump(py_data, f, indent=4, ensure_ascii=False,)
# 读取数据
msg = open('./练习文件/json.json', 'r', encoding='utf-8')
msg = json.load(msg)
print(msg)