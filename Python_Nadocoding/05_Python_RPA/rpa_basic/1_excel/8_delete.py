from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8)     # 8번째 줄의 7번 학생의 데이터를 삭제
# ws.delete_rows(8, 3)  # 8번째 줄부터 아래로 총 3 줄 삭제

# ws.delete_cols(2)     # 2번째 열 (= B) 삭제
ws.delete_cols(2, 2)  # 2번째 열로부터 2개 열 삭제

wb.save("sample_delete_col.xlsx")