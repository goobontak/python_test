import pandas as pd
import tkinter as tk
 
window = tk.Tk()
window.title("노선도")
window.geometry("1500x1500")
img = tk.PhotoImage(file="C:\python\전철 노선도.png")
bg_img = tk.Label(image=img)
bg_img.pack(expand="True",fill="both")

# 엑셀 파일 불러오기
excel_file = pd.read_excel('C:\python\노선도.xlsx', sheet_name='Sheet1')

# 검색어
value= input()
value2= input()

# 검색하여 결과 출력
result = excel_file[excel_file.iloc[:, 0].str.contains(value)]
result2 = excel_file[excel_file.iloc[:, 0].str.contains(value2)]

# 역코드 값을 가져와서 value 값이큰 것에서 작은 것을 뺀 값을 출력
if len(result) > 0 and len(result2) > 0:
    code1 = result.iloc[0][5]
    code2 = result2.iloc[0][5]
    
    diff = abs(code1 - code2)*3
    diff=diff%100
    print(f"{diff}분")
else:
    print("검색 결과가 없습니다.") 