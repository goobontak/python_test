import tkinter

# 좌표를 저장할 리스트 생성
A = (145,277,121,301)
B = (225,277,201,301)
C = (300,277,276,301)
D = (380,277,356,301)
E = (465,277,441,301)
F = (545,277,521,301)
G = (620,277,596,301)
H = (705,277,681,301)
I = (785,277,761,301)
J = (860,277,836,301)
K = (945,277,921,301)
L = (1020,277,996,301)
M = (1105,277,1081,301)
N = (1180,277,1156,301)
O = (1265,277,1241,301)
P = (1340,277,1316,301)
Q = (1425,277,1401,301)

station_positions = []
print(station_positions) #확인용

station_positions.append(A)
station_positions.append(B)
station_positions.append(C)
station_positions.append(D)
station_positions.append(E)
station_positions.append(F)
station_positions.append(G)
station_positions.append(H)
station_positions.append(I)
station_positions.append(J)
station_positions.append(K)
station_positions.append(L)
station_positions.append(M)
station_positions.append(N)
station_positions.append(O)
station_positions.append(P)
station_positions.append(Q)



window = tkinter.Tk()
window.title("지하철 노선") 
window.geometry("1600x1000")
img = tkinter.PhotoImage(file="8호선.png")

canvas = tkinter.Canvas(window, relief="solid", width=1800, height=500)
Img = canvas.create_image([800, 250], anchor="center", image=img)
canvas.place(x=0, y=0)

oval_1_coords = station_positions[0]
oval_2_coords = station_positions[1]
oval_3_coords = station_positions[2]
oval_4_coords = station_positions[3]
oval_5_coords = station_positions[4]
oval_6_coords = station_positions[5]
oval_7_coords = station_positions[6]
oval_8_coords = station_positions[7]
oval_9_coords = station_positions[8]
oval_10_coords = station_positions[9]
oval_11_coords = station_positions[10]
oval_12_coords = station_positions[11]
oval_13_coords = station_positions[12]
oval_14_coords = station_positions[13]
oval_15_coords = station_positions[14]
oval_16_coords = station_positions[15]
oval_17_coords = station_positions[16]

print(oval_1_coords) #확인용
print(oval_2_coords)
print(oval_3_coords)
print(oval_4_coords) 


oval_1 = canvas.create_oval(oval_1_coords, fill="black", state='hidden',width=0)
oval_2 = canvas.create_oval(oval_2_coords, fill="black", state='hidden',width=0)
oval_3 = canvas.create_oval(oval_3_coords, fill="black", state='hidden',width=0)
oval_4 = canvas.create_oval(oval_4_coords, fill="black", state='hidden',width=0)
oval_5 = canvas.create_oval(oval_5_coords, fill="black", state='hidden',width=0)
oval_6 = canvas.create_oval(oval_6_coords, fill="black", state='hidden',width=0)
oval_7 = canvas.create_oval(oval_7_coords, fill="black", state='hidden',width=0)
oval_8 = canvas.create_oval(oval_8_coords, fill="black", state='hidden',width=0)
oval_9 = canvas.create_oval(oval_9_coords, fill="black", state='hidden',width=0)
oval_10 = canvas.create_oval(oval_10_coords, fill="black", state='hidden',width=0)
oval_11 = canvas.create_oval(oval_11_coords, fill="black", state='hidden',width=0)
oval_12 = canvas.create_oval(oval_12_coords, fill="black", state='hidden',width=0)
oval_13 = canvas.create_oval(oval_13_coords, fill="black", state='hidden',width=0)
oval_14 = canvas.create_oval(oval_14_coords, fill="black", state='hidden',width=0)
oval_15 = canvas.create_oval(oval_15_coords, fill="black", state='hidden',width=0)
oval_16 = canvas.create_oval(oval_16_coords, fill="black", state='hidden',width=0)
oval_17 = canvas.create_oval(oval_17_coords, fill="black", state='hidden',width=0)

    
ovals=[]
print(ovals) #확인용

count=[]
str_ovals=[]

def select_station1():
    oval_1_coords = station_positions[0]
    ovals.append(oval_1_coords)
    canvas.coords(oval_1, oval_1_coords)
    canvas.itemconfig(oval_1, state='normal')
    str_ovals.append('oval_1')
    count.append('1')

def select_station2():
    oval_2_coords = station_positions[1]
    ovals.append(oval_2_coords)
    canvas.coords(oval_2, oval_2_coords)
    canvas.itemconfig(oval_2, state='normal')
    count.append('2')

def select_station3():
    oval_3_coords = station_positions[2]
    ovals.append(oval_3_coords)
    canvas.coords(oval_3, oval_3_coords)
    canvas.itemconfig(oval_3, state='normal')
    str_ovals.append('oval_3')
    count.append('3')


def select_station4():
    oval_4_coords = station_positions[3]
    ovals.append(oval_4_coords)
    canvas.coords(oval_4, oval_4_coords)
    canvas.itemconfig(oval_4, state='normal')
    count.append('4')
    
def select_station5():
    oval_5_coords = station_positions[4]
    ovals.append(oval_5_coords)
    canvas.coords(oval_5, oval_5_coords)
    canvas.itemconfig(oval_5, state='normal')
    count.append('5')
    

def select_station6():
    oval_6_coords = station_positions[5]
    ovals.append(oval_6_coords)
    canvas.coords(oval_6, oval_6_coords)
    canvas.itemconfig(oval_6, state='normal')
    count.append('6')
  
def select_station7():
    oval_7_coords = station_positions[6]
    ovals.append(oval_7_coords)
    canvas.coords(oval_7, oval_7_coords)
    canvas.itemconfig(oval_7, state='normal')
    count.append('7')
  

def select_station8():
    oval_8_coords = station_positions[7]
    ovals.append(oval_8_coords)
    canvas.coords(oval_8, oval_8_coords)
    canvas.itemconfig(oval_8, state='normal')
    count.append('8')
  
def select_station9():
    oval_9_coords = station_positions[8]
    ovals.append(oval_9_coords)
    canvas.coords(oval_9, oval_9_coords)
    canvas.itemconfig(oval_9, state='normal')
    count.append('9')
   
def select_station10():
    oval_10_coords = station_positions[9]
    ovals.append(oval_10_coords)
    canvas.coords(oval_10, oval_10_coords)
    canvas.itemconfig(oval_10, state='normal')
    count.append('10')
   

def select_station11():
    oval_11_coords = station_positions[10]
    ovals.append(oval_11_coords)
    canvas.coords(oval_11, oval_11_coords)
    canvas.itemconfig(oval_11, state='normal')
    count.append('11')
   
def select_station12():
    oval_12_coords = station_positions[11]
    ovals.append(oval_12_coords)
    canvas.coords(oval_12, oval_12_coords)
    canvas.itemconfig(oval_12, state='normal')
    count.append('12')
   
def select_station13():
    oval_13_coords = station_positions[12]
    ovals.append(oval_13_coords)
    canvas.coords(oval_13, oval_13_coords)
    canvas.itemconfig(oval_13, state='normal')
    count.append('13')
  

def select_station14():
    oval_14_coords = station_positions[13]
    ovals.append(oval_14_coords)
    canvas.coords(oval_14, oval_14_coords)
    canvas.itemconfig(oval_14, state='normal')
    count.append('14')
   

def select_station15():
    oval_15_coords = station_positions[14]
    ovals.append(oval_15_coords)
    canvas.coords(oval_15, oval_15_coords)
    canvas.itemconfig(oval_15, state='normal')
    count.append('15')
  

def select_station16():
    oval_16_coords = station_positions[15]
    ovals.append(oval_16_coords)
    canvas.coords(oval_16, oval_16_coords)
    canvas.itemconfig(oval_16, state='normal')
    count.append('16')
  

def select_station17():
    oval_17_coords = station_positions[16]
    ovals.append(oval_17_coords)
    canvas.coords(oval_17, oval_17_coords)
    canvas.itemconfig(oval_17, state='normal')
    count.append('17') 
  

# 출발역 선택 메뉴버튼 생성
startmenu = tkinter.Menubutton(window, text="출발역 선택", font=("Verdana", 18, "bold"),direction="right")
startmenu.place(x=38, y=390)
s_menu = tkinter.Menu(startmenu, tearoff=0)
s_menu.add_command(label="암             사", font=("Verdana", 18, "bold"),command=select_station1)
s_menu.add_command(label="천             호", font=("Verdana", 18, "bold"),command=select_station2)
s_menu.add_command(label="강  동   구  청", font=("Verdana", 18, "bold"),command=select_station3)
s_menu.add_command(label="몽  촌   토  성", font=("Verdana", 18, "bold"),command=select_station4)
s_menu.add_command(label="잠             실", font=("Verdana", 18, "bold"),command=select_station5)
s_menu.add_command(label="석             촌", font=("Verdana", 18, "bold"),command=select_station6)
s_menu.add_command(label="송             파", font=("Verdana", 18, "bold"),command=select_station7)
s_menu.add_command(label="가  락   시  장", font=("Verdana", 18, "bold"),command=select_station8)
s_menu.add_command(label="문             정", font=("Verdana", 18, "bold"),command=select_station9)
s_menu.add_command(label="장             지", font=("Verdana", 18, "bold"),command=select_station10)
s_menu.add_command(label="복             정", font=("Verdana", 18, "bold"),command=select_station11)
s_menu.add_command(label="산             성", font=("Verdana", 18, "bold"),command=select_station12)
s_menu.add_command(label="남한산성 입구", font=("Verdana", 18, "bold"),command=select_station13)
s_menu.add_command(label="단 대 오 거 리", font=("Verdana", 18, "bold"),command=select_station14)
s_menu.add_command(label="신             흥", font=("Verdana", 18, "bold"),command=select_station15)
s_menu.add_command(label="수             진", font=("Verdana", 18, "bold"),command=select_station16)
s_menu.add_command(label="모             란", font=("Verdana", 18, "bold"),command=select_station17)
startmenu["menu"] = s_menu


        
#도착역선택 메뉴버튼 생성
endmenu = tkinter.Menubutton(window, text="도착역 선택", font=("Verdana", 18, "bold"),direction="right")
endmenu.place(x=200,y=390)
e_menu=tkinter.Menu(endmenu,tearoff=0)
e_menu.add_command(label="암             사", font=("Verdana", 18, "bold"),command=select_station1)
e_menu.add_command(label="천             호", font=("Verdana", 18, "bold"),command=select_station2)
e_menu.add_command(label="강  동   구  청", font=("Verdana", 18, "bold"),command=select_station3)
e_menu.add_command(label="몽  촌   토  성", font=("Verdana", 18, "bold"),command=select_station4)
e_menu.add_command(label="잠             실", font=("Verdana", 18, "bold"),command=select_station5)
e_menu.add_command(label="석             촌", font=("Verdana", 18, "bold"),command=select_station6)
e_menu.add_command(label="송             파", font=("Verdana", 18, "bold"),command=select_station7)
e_menu.add_command(label="가  락   시  장", font=("Verdana", 18, "bold"),command=select_station8)
e_menu.add_command(label="문             정", font=("Verdana", 18, "bold"),command=select_station9)
e_menu.add_command(label="장             지", font=("Verdana", 18, "bold"),command=select_station10)
e_menu.add_command(label="복             정", font=("Verdana", 18, "bold"),command=select_station11)
e_menu.add_command(label="산             성", font=("Verdana", 18, "bold"),command=select_station12)
e_menu.add_command(label="남한산성 입구", font=("Verdana", 18, "bold"),command=select_station13)
e_menu.add_command(label="단 대 오 거 리", font=("Verdana", 18, "bold"),command=select_station14)
e_menu.add_command(label="신             흥", font=("Verdana", 18, "bold"),command=select_station15)
e_menu.add_command(label="수             진", font=("Verdana", 18, "bold"),command=select_station16)
e_menu.add_command(label="모             란", font=("Verdana", 18, "bold"),command=select_station17)
endmenu["menu"]=e_menu


# 이후, 리스트에 저장된 좌표들을 이용해 다른 함수에서 사용할 수 있습니다.
        
def connect_ovals():
    # 라인 그리기
    global count
    global line_1
    line_1= canvas.create_line(ovals[0][0]-5, ovals[0][3]-11, ovals[1][2]+5, ovals[1][3]-11, width=10, fill="black")
    print(connect_ovals)
    global lead_time
    lead_time = abs(int(count[1])-int(count[0]))*2
    lead_time_label.config(text=str(lead_time)+"분 예상됩니다.")
    

def clear():
    canvas.itemconfig(oval_1, state='hidden')
    canvas.itemconfig(oval_2, state='hidden')
    canvas.itemconfig(oval_3, state='hidden')
    canvas.itemconfig(oval_4, state='hidden')
    canvas.itemconfig(oval_5, state='hidden')
    canvas.itemconfig(oval_6, state='hidden')
    canvas.itemconfig(oval_7, state='hidden')
    canvas.itemconfig(oval_8, state='hidden')
    canvas.itemconfig(oval_9, state='hidden')
    canvas.itemconfig(oval_10, state='hidden')
    canvas.itemconfig(oval_11, state='hidden')
    canvas.itemconfig(oval_12, state='hidden')
    canvas.itemconfig(oval_13, state='hidden')
    canvas.itemconfig(oval_14, state='hidden')
    canvas.itemconfig(oval_15, state='hidden')
    canvas.itemconfig(oval_16, state='hidden')
    canvas.itemconfig(oval_17, state='hidden')
    canvas.delete(line_1)
        
    lead_time_label.config(text="")
    
    
tkinter.Button(window,text='초 기 화', font=("Verdana", 18, "bold"), command=clear).place(x=550,y=390)
    
# 캔버스에 출력
lead_time_label = tkinter.Label(window, font=("Verdana", 18, "bold"))
lead_time_label.place(x=180,y=462)

lead_time = tkinter.Menubutton(window, text="소요시간은", font=("Verdana", 18, "bold"))
lead_time.place(x=40,y=460)

   
#선택완료 메뉴버튼 생성   
draw = tkinter.Menubutton(window, text="경 로 설 정", font=("Verdana", 18, "bold"),direction="right")
draw.place(x=380,y=390)
draw_menu=tkinter.Menu(draw,tearoff=0)
#경로확인 메뉴 클릭 시 draw_line() 함수 호출
draw_menu.add_command(label="선 택  완 료", font=("Verdana", 18, "bold"), command=connect_ovals)
draw["menu"]=draw_menu


    
window.mainloop()