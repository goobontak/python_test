# r - 읽기전용 / w- 쓰기 / x - 베타적 / a - 이어쓰기 / b - 바이너리(2진수) /  t - 텍스트 전용 / + 읽기,쓰기 파일열기
# open(file,mode='r',buffering =-1, endoding='언어', error'None' ,new=None)


a_file = open("global.txt","w",encoding="UTF-8")
print("과정 : 스마트융합",file=a_file)
print("날짜 : 23년 02월 13일",file=a_file)
print("내용 : 파이썬 파일 출력",file=a_file)
a_file.close()

b_file= open("global.txt","a",encoding="UTF-8")
print("시간 : 09:00~ 17:40 ",file=b_file)
b_file.write("간식메뉴 : 붕어빵\n")
b_file.write("음료메뉴\n : 아아,아샷추")
b_file.close()