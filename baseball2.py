from random import *
com = []
for i in range(4): 
    x = randint(1,9) 
    while x in com:
         x = randint(1,9)    
    com.append(x)  
print(com) 
cnt = 0
while cnt <10:
    me = list(map(int,input('숫자를 모두 입력하세요 : ').split(" ")))
    strike = 0
    ball = 0
    for i in range(4):
        for j in range(4):
            if me[i] == com[j]:
                if(i == j):
                    strike +=1
                if(i != j):
                    ball +=1
    print("{}strike {}ball".format(strike,ball))
    cnt+=1
    if strike == 4:
        print("홈런~~~~~~~")
        break

if cnt==10:
    print("10번의 기회를 다하셨습니다.")
    
