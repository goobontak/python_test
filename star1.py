for i in range(0,7,1):
    for j in range(7-i): #빈칸
        print("  ",end="")
    for j in range(0,1+i*2,1):
        print("☆ ",end="")
    print('')
for i in range(8):
    for j in range(i): #빈칸
        print("  ",end="")
    for j in range(15,i*2,-1):
        print("☆ ",end="")
    print('') 
    
print()
for i in range(1,17,2):
    print('{:^30}'.format('☆ '*i))      
for i in range(13,0,-2):
    print('{:^30}'.format('☆ '*i))
 