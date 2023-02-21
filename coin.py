money = int(input('동전개수 구하기: '))
coin = money
coin = coin/50000 
money = money % 50000
if int(coin) != 0:
    print('5만원 개수 : ',int(coin))
    print(money)

coin= money
money = money % 10000
coin = coin /10000
if int(coin) != 0:
    print('1만원 개수 : ',int(coin))
    print(money)

coin = money
money = money % 5000
coin = coin/5000
if int(coin) != 0:
    print('5천원 개수 : ',int(coin))
    print(money)

coin = money
money = money % 1000
coin = coin/1000
if int(coin) != 0:
    print("1천원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 500
coin = coin/500
if int(coin) != 0:
    print("500원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 100
coin = coin/100
if int(coin) != 0:
    print("100원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 50
coin = coin/50
if int(coin)!= 0:
    print("50원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 10
coin = coin/10
if int(coin) != 0:
    print("10원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 5
coin = coin/5
if int(coin) != 0:
    print("5원 개수 : ",int(coin))
    print(money)

coin = money
money = money % 1
coin = coin/1
if int(coin) != 0:
    print("1원 개수 : ",int(coin))
    print(money)