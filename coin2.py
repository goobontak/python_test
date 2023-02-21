money = int(input('동전개수 구하기: '))
print()

print("1원의 경우의 수 ") # 1원 경우의 수
money_1 = money / 1 
print(" 1원 개수 : ",int(money_1)) 
print()


print('5,1원 경우의 수 ')  # 1,5원 경우의 수 
money_2 = money
money_2= money/5  
print(" 5원 개수 :",int(money_2))
money_2 =money %5
print(" 1원 개수 :",int(money_2))
print()

print("10원,5원,1원 경우의 수 ")  # 1,5,10원 경우의 수
money_3 = money   
money_3= money / 10
print("10원 개수 : ",int(money_3))
money_3= money_3 % 10
money_3= money_3 /5
print(" 5원 개수 : ",int(money_3))
money_3= money % 5
print(" 1원 개수 : ",int(money_3))
print()


print("50원,10원,5원,1원 경우의 수 ") # 1,5,10,50원 경우의 수
money_4 = money 
money_4 = money / 50
print("50원 개수  : ",int(money_4))
money_4 = money_4 % 50
print(money_4)
money_4 = money_4 / 10
print("10원 개수  : ",int(money_4))
money_4 = money_4 % 10
money_4 = money_4 / 5
print(" 5원 개수  : ",int(money_4))
money_4 = money % 1
print("10원 개수  : ",int(money_4))
print()