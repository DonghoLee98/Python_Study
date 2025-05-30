from openpyxl import Workbook
wb = Workbook()
ws = wb.active

# https://www.youtube.com/watch?v=exgO1LFl9x8&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=8
# 2:01:25, 챕터 20.퀴즈








wb.save("scores.xlsx")