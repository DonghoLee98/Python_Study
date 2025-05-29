from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 번호, 영어, 수학
a1 = ws["A1"]   # 번호
b1 = ws["B1"]   # 영어
c1 = ws["C1"]   # 수학

# A column의 너비를 5로 지정
ws.column_dimensions["A"].width = 5

wb.save("sample_style.xlsx")

# https://www.youtube.com/watch?v=exgO1LFl9x8&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=7
# 1:30:23