import PyPDF2
import pdfplumber
from openpyxl import Workbook

# 1. 利用 pdfplumber 提取文字
with pdfplumber.open('../EXData/自动化办公手册.pdf') as p:
    page = p.pages[27]
    print(page.extract_text())

# 2. 利用 pdfplumber 提取表格并写入 excel'''
#     table = page.extract_table()
#     print(table)
#     workbook = Workbook()
#     sheet = workbook.active
#     for row in table:
#         if not "".join([str(i) for i in row]) == "":  # 将列表中每个元素都连接成一个字符串，如果还是一个空字符串就去掉空行。
#             sheet.append(row)
#     workbook.save(filename="新 pdf.xlsx")

# 3. 合并pdf
