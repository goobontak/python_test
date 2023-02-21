etc = 'tuple'
bt=('123','64659')
at=('23','1241',bt)
tp = ('★','1512',at)
Array = (123 , "가나다라",etc,tp)

print(Array)
print(Array[3][2][2][1][4])
print("이거뭐야",type(Array))

(name,age,hobby)=("임승현","20",("game","language"))
print(age,name,hobby)

print(etc)
print(tp)

etc,tp=tp,etc

print(etc)
print(tp)
a=4
b=2
a,b=b,a
print(a)
print(b)

ap='ap'
ad='ad'
ad,ap=ap,ad
print(ap)
print(ad)
