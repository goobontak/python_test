from random import *

my_ball = list(map(int,input('숫자를 모두 입력하세요 : ').split(" ")))
ball=[]
while len(ball) < 3:
    su = randint(1,9)
    if su not in ball:
        ball.append(su)
        
print(ball)
print(my_ball)
print(type(my_ball))
print(type(ball))

strike=0
ball=0

for x in range(3):
        if(my_ball[x] == ball[x]):
            strike +=1
   
            

for x in range(3):
    for i in range(3):
        if(my_ball[x]==ball[i]):
            ball+=1
            
print(strike+"스트라이크"+ball+"볼" )
