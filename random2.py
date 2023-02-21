from random import *
gold_hand = input("번호를 입력하시오").split(" ")
num=[]
while len(num) < 6:
    su = randint(1,45)
    if su not in num:
        num.append(su)

print(num)
gold_hand=list(map(int,gold_hand))
gold_hand.sort()
num.sort()

lotto = list(set(gold_hand)-set(num))

if len(lotto)==0:
    print("1등입니다.")
elif len(lotto)==1:
    print("2등입니다.")
elif len(lotto)==2:
    print("3등입니다.")
elif len(lotto)==3:
    print("4등입니다.")
elif len(lotto)==4:
    print("5등입니다.")    
else:
    print("당첨되지 않았습니다.")

print("행운의 로또",lotto)
print(type(lotto))
print(gold_hand)
print(type(gold_hand))
print(num)
print(type(num))



