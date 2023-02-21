from math import *
in_car = (input("출입시간 : ").split(':'))
out_car = (input("출입시간 : ").split(':'))

in_car=list(map(int,in_car))
out_car=list(map(int,out_car))

in_car_time= in_car[0]*60+in_car[1]
out_car_time= out_car[0]*60+out_car[1]

time = out_car_time-in_car_time

money=300

if(time<30):
    print("30분 미만 무료주차")
elif(time>=30):
        time-=30
        cnt =ceil(time/10)
        pay = cnt*money
print('총 주차요금은 ',pay,"원 입니다.")

    
     
