num=int(input('몇개 입력할꺼야?'))
5

for i in range(0,num):
    for j in range(0,i+1,1):
        print("★ ",end="")
    for j in range(num-i-1): 
        print("  ",end="")
    for j in range(num,i,-1):
        print("★ ",end="")
    for j in range(i): 
        print("  ",end="")
    print('')        
    
for i in range(0,num):
    for j in range(num,i+1,-1):
        print("  ",end="")
    for j in range(i+1): 
        print("★ ",end="")
    for j in range(0,i,1):
        print("  ",end="")
    for j in range(num-i): 
        print("★ ",end="")
    print('')
for i in range(0,num):
    for j in range(num*2,i+1,-1):
        print(" ",end="")
    for j in range(i+1): 
        print("★ ",end="")
    print()
    
       