str = "abcde"
for x in str:
    print(x)

set = [30,31,32]
for x in set:
    print(x)

dict = {'one' : 1, 'two' : 2 , 'three' : 3}
for x in dict:
    print(x) # 키값
for x in dict:
    print(dict.get(x)) # 값
    
for [x,y] in [[1,2],[3,4],[5,6]]:
    print(y,x)