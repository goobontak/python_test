import pandas as pd
import tkinter as tk
 
window = tk.Tk()
window.title("노선도")
window.geometry("1020x1000")
img = tk.PhotoImage(file="C:\python\지하철 노선도.png")
bg_img = tk.Label(image=img)
bg_img.pack(side="right")

frame3=tk.Frame(window,width=600,height=800,bg='yellow')
frame3.place(x=20,y=250)
frame1=tk.Frame(window,width=100,height=80,relief='solid',bd=2)
frame2=tk.Frame(window,width=200,height=80,relief='solid',bd=2)
frame1.place(x=20,y=100)
frame2.place(x=400,y=100)
name=tk.Label(text="안녕하세요",font="굴림체").pack()
start_station1= tk.Label(frame1,text="출발역")
start_station = tk.Entry(frame1,width=30)
start_station1.pack()
start_station.pack()

end_station1= tk.Label(frame2,text="도착역")
end_station = tk.Entry(frame2,width=30)
end_station1.pack()
end_station.pack()





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