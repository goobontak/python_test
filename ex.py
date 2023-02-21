

my_ball =[1,2,3,4]
ball=[1,2,3,4]
strike=0
for x in range(3):
        if(my_ball[x] == ball[x]):
            strike +=1

print(strike)
print(my_ball)
print(type(my_ball))
print(ball)
print(type(ball)) 



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