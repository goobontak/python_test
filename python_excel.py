from openpyxl import load_workbook

# 엑셀 파일 불러오기
wb = load_workbook('C:\python\python_excel.xlsx')

# 시트 선택
ws = wb.active

# 셀 데이터 출력
for row in ws.rows:
    for cell in row:
        print(cell.value)
        