from random import *
ar_input = list(map(int,input('숫자를 모두 입력하세요 : ').split(" ")))
ar_set = []
for i in range(6): 
    x = randint(1,45) 
    while x in ar_set:
         x = randint(1,45)    
    ar_set.append(x)  
print(ar_set)  
cnt = 0
for x in range(6):
    for i in range(6):
        if(ar_input[x] == ar_set[i]):
            cnt+=1
print("맞은갯수 : ",cnt)
if cnt==6:
    print("1등 - 50억")
elif cnt==5:
    print("3등 - 500만원")
elif cnt==4:
    print("4등 - 5만원")
elif cnt ==3:
    print("5등 - 5천원")
else:
    print("당첨되지 않았습니다.")

com = [1,2,3]
me = [3,2,4]
strike = 0
ball = 0
for i in range(3):
    for j in range(3):
        if me[i] == com[j]:
            if(i == j):
                strike +=1
            if(i != j):
                ball +=1
                
print("{}strike {}ball".format(strike,ball))
        