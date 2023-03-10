import pprint
from xml.etree import ElementTree as ET

tree = ET.parse('E:/NodeVScode/09.python_data/EXData/data03XML.xml')
# 解析传入文件的数据
root = tree.getroot()
# 获取树的根元素

data = root.find('Data')

all_data = []

for observation in data:
    record = {}
    for item in observation:
        lookup_key_List = list(item.attrib.keys())
        lookup_key = lookup_key_List[0]

        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        record[rec_key] = rec_value

    all_data.append(record)

pprint.pprint(all_data)