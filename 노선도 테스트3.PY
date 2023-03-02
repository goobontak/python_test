import pandas as pd
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
import time
import datetime

# 엑셀 파일 불러오기
excel_file = pd.read_excel('C:\python\노선도.xlsx', sheet_name='Sheet1')

# tkinter 윈도우 생성
window = tk.Tk()
window.title("노선도")
window.geometry("1920x1200")
window.state('zoomed')
window.configure(background='white')

trans = tk.Label(window, width=50, height=50, bg='white')
trans.place(x=-100, y=-100)
transs1 = ImageTk.PhotoImage(file="C:\python\환승역 이미지_누끼제거.png")
trans.config(image=transs1)

trans2 = tk.Label(window, width=50, height=50, bg='white')
trans2.place(x=-100, y=-100)
transs2 = ImageTk.PhotoImage(file="C:\python\환승역 이미지_누끼제거.png")
trans2.config(image=transs2)

trans3 = tk.Label(window, width=50, height=50, bg='white')
trans3.place(x=-100, y=-100)
transs3 = ImageTk.PhotoImage(file="C:\python\화장실 이미지_누끼제거.png")
trans3.config(image=transs3)

trans4 = tk.Label(window, width=50, height=50, bg='white')
trans4.place(x=-100, y=-100)
transs4 = ImageTk.PhotoImage(file="C:\python\화장실 이미지_누끼제거.png")
trans4.config(image=transs4)

# 검색 결과를 출력할 텍스트 박스 생성
result_text1 = tk.Text(window, height=20, width=73,bd=0)
result_text1.place(x=100, y=200)

result_text2 = tk.Text(window, height=20, width=73,bd=0)
result_text2.place(x=100, y=500)

result_text3 = tk.Text(window, height=20, width=73,bd=0)
result_text3 = tk.Text(window, height=20, width=73,bd=0)
result_text3.place(x=100, y=800)

def mouse_click(event):
    x, y = event.x, event.y
    print("x:", x, "y:", y)

def clear_entries():
    start_station.delete(0, tk.END)
    end_station.delete(0, tk.END)
    result_text1.delete('1.0', tk.END)
    result_text2.delete('1.0', tk.END)
    result_text3.delete('1.0', tk.END)
    start_button.destroy()
    end_button.destroy()  
    trans.place_configure(x=-100,y=-100)
    trans2.place_configure(x=-100,y=-100)
    trans3.place_configure(x=-100,y=-100)
    trans4.place_configure(x=-100,y=-100)
    
    
    
def set_marker_on_button(button, image_file):
    img = ImageTk.PhotoImage(file=image_file)
    button.image = img
    button.config(image=img)
    
    
def set_marker_on_map(map, image_file):
    map2 = ImageTk.PhotoImage(file=image_file)
    map.image = map2
    map.config(image=map2)
    
def search(*args):
    global start_button
    global end_button
    global trans
    global trans2
    global trans3
    global trans4
   
    
    start = start_station.get()
    end = end_station.get()
    
    result = excel_file[excel_file.iloc[:, 0].str.contains(start, na=False)]
    result2 = excel_file[excel_file.iloc[:, 0].str.contains(end, na=False)]

    # 검색된 결과가 있을 경우 해당 역의 행 정보 출력
    if len(result) > 0 and len(result2) > 0:
        new_font = Font(size=24, weight="bold")
        result_text1.delete("1.0", tk.END)  # 이전 검색 결과 삭제
        result_text1.insert(tk.END, "                   출발역 정보\n\n")
        result_text1.insert(tk.END, result.iloc[0]["역"]+"\n\n")
        result_text1.insert(tk.END, result.iloc[0]["주소"]+"\n")
        result_text1.insert(tk.END, result.iloc[0]["전화번호"])
        result_text1.configure(font=new_font)
        
        result_text2.delete("1.0", tk.END)  # 이전 검색 결과 삭제
        result_text2.insert(tk.END, "                   도착역 정보\n\n")
        result_text2.insert(tk.END, result2.iloc[0]["역"]+"\n\n")
        result_text2.insert(tk.END, result2.iloc[0]["주소"]+"\n")
        result_text2.insert(tk.END, result2.iloc[0]["전화번호"]+"\n")
        result_text2.configure(font=new_font)
                
        canvas = tk.Label(window, width=image.width, height=image.height)
        canvas.place(x=700, y=7)
        set_marker_on_map(canvas, "C:\python\지하철 노선도.png")
        
            
            
        start_button = tk.Label(window, width=50, height=50, bg="white")
        start_x, start_y = result.iloc[0]["x좌표"], result.iloc[0]["y좌표"]
        start_button.place(x=start_x+700, y=start_y+8)
        set_marker_on_button(start_button, "C:\python\빨간_도착지_핀_이미지-누끼제거.png")
        
        
        # 도착역 이미지에 마커 표시
        end_button = tk.Label(window, width=50, height=50, bg="white")
        end_x, end_y = result2.iloc[0]["x좌표"], result2.iloc[0]["y좌표"]
        end_button.place(x=end_x+700, y=end_y+8)
        set_marker_on_button(end_button, "C:\python\빨간_도착지_핀_이미지-누끼제거.png")
        
    if len(result) > 0 and len(result2) > 0:
        code1 = result.iloc[0]["역코드"]
        code2 = result2.iloc[0]["역코드"]
        diff = abs(code1 - code2)*3
        
        current_time = time.strftime("출발시간 :  %H 시 %M 분 \n")
        result_text3.delete("1.0", tk.END)
        result_text3.insert(tk.END, current_time)
        result_text3.insert(tk.END,"소요시간 :  ")
        result_text3.insert(tk.END,round(diff))
        result_text3.insert(tk.END," 분\n")
        result_text3.insert(tk.END,"도착시간 : ")
        result_text3.configure(font=new_font)
        current_time = datetime.datetime.strptime(time.strftime("%H:%M"), "%H:%M")
        new_time = current_time + datetime.timedelta(minutes=int(diff))
        new_time_int = new_time.strftime(" %H 시 %M 분")
        print(new_time_int)
        result_text3.insert(tk.END,new_time_int)
        
        print(result.iloc[0]["환승"])
        
    if result.iloc[0]["환승"] == int(1):
        trans.place_configure(x=340, y=270)

    if result2.iloc[0]["환승"] == int(1):
        trans2.place_configure(x=340, y=570)

    if result.iloc[0]["화장실"] == int(1):
        trans3.place_configure(x=440, y=270)

    if result2.iloc[0]["화장실"] == int(1):
        trans4.place_configure(x=440, y=570)

# 이미지 출력을 위한 canvas 생성
image = Image.open("C:\python\지하철 노선도.png")
photo = ImageTk.PhotoImage(image)
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.pack(side="right")
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

new_image = Image.open("C:\python\수도권_전철노선도_제목-removebg-preview.png")
new_photo = ImageTk.PhotoImage(new_image)
new_canvas = tk.Canvas(window, width=new_image.width, height=new_image.height, bg='white')
new_canvas.pack(pady=7)
new_canvas.create_image(0, 0, image=new_photo, anchor=tk.NW)

# 출발역, 도착역 입력 받기
frame1 = tk.Frame(window, width=100, height=80, relief='solid', bd=2)
frame2 = tk.Frame(window, width=200, height=80, relief='solid', bd=2)
frame1.place(x=60, y=120)
frame2.place(x=300, y=120)

start_station1 = tk.Label(frame1, text="출발역")
start_station = tk.Entry(frame1, width=30)
start_station1.pack()
start_station.pack()

end_station1 = tk.Label(frame2, text="도착역")
end_station = tk.Entry(frame2, width=30)
end_station1.pack()
end_station.pack()

# 초기화 버튼 생성
clear_button = tk.Button(window, text="초기화", command=clear_entries, width=5, height=2)
clear_button.place(x=600, y=120)

# 검색 버튼 생성
search_button = tk.Button(window, text="검색", command=search, width=5, height=2)
search_button.place(x=540, y=120)



# Enter 키 바인딩
start_station.bind('<Return>', search)
end_station.bind('<Return>', search)
canvas.bind("<Button-1>", mouse_click)

window.mainloop()