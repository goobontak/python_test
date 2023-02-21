name="이순신"
job="hero"
grade = 2

print(name+"장군은 타이틀이 "+job+" 이고 ",grade,"등급 이십니다.")
print(name+"장군은 타이틀이 "+job+" 이고 "+str(grade)+"등급 이십니다.")

a=10
b=7
print(3==3)
print(3!=3)
print((a<20) and (b<10))

c=1<3 #ture=1 / 1+1=2 -> c=2
c+=1
print(c)

i="1234"
i2="1234"
i3=1234
i4=1234
print(i[2])
print(i[2]==i2[2])
print(str(i3)[3]==str(i4)[3])
print(len(i))

today="20230127"
print("이번년도 "+today[0:4]+"년 입니다")
print("지금은 "+today[6:8]+"일 입니다")
print(today[-1])

print("%d년은 %s년이다" %(2023,'계묘'))
print("{}{}")
a='구'
b='본'
print(f"{a}{b}")

