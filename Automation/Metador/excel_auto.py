from openpyxl import Workbook
from win32com.client import Dispatch

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "max"

workbook.save(filename="hello.xlsx")

cell = sheet["A1"]
cell.value = "Greetings"

print(cell.value)

workbook.save(filename="hello.xlsx")

xl = Dispatch("Excel.Application")
xl.Visible = True

wb = xl.Workbooks.Open(r'hello.xlsx')