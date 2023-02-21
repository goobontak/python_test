from random import *
ar_input = list(map(int,input('숫자를 모두 입력하세요 : ').split(" ")))
ar_set = []
for i in range(6): 
    x = randint(1,45) 
    while x in ar_set:
         x = randint(1,45)    
    ar_set.append(x)  
print(type(ar_set))
print(type(ar_input))
cnt = 0
for x in range(6):
    for i in range(6):
        if(ar_input[x] == ar_set[i]):
            cnt+=1
print("맞은갯수 : ",cnt)



'''
ar_input = []

for x in range(6):
    num  = input('숫자를 입력하세요 : ')
    ar_input.append(int(num))
print(ar_input)

if ar_input[0] == 1:
    print("같아")
else:
    print("달라")
    
   ''' 
    
    


