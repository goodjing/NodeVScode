import os

import PyPDF2
import pdfplumber
from PyPDF2 import PdfFileWriter, PdfFileReader
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
# pdf_writer = PdfFileWriter()
# for i in range(1, len(os.listdir(r"G:\6Tipdm\7python 办公自动化\concat_pdf")) + 1):
#     print(i * 50 + 1, (i + 1) * 50)
#     pdf_reader = PdfFileReader("G:\\6Tipdm\\7python 办公自动化\\concat_pdf\{}-{}.pdf".format(i * 50 + 1, (i + 1) * 50))
#     for page in range(pdf_reader.getNumPages()):
#         pdf_writer.addPage(pdf_reader.getPage(page))
# with open("G:\\6Tipdm\\7python 办公自动化\\concat_pdf\merge.pdf", "wb") as out:
#     pdf_writer.write(out)

# 4. 拆分pdf
# pdf_reader = PdfFileReader(r"G:\6Tipdm\7python 办公自动化\concat_pdf\时间序列.pdf")
# for page in range(pdf_reader.getNumPages()):
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(pdf_reader.getPage(page))
#     with open(f"G:\\6Tipdm\\7python 办公自动化\\concat_pdf\\{page}.pdf", "wb") as out: pdf_writer.write(out)
