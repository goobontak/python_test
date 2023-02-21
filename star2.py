for i in range(8):
    for j in range(15,i*2,-1):
        print("☆ ",end="")
    for j in range(i): #빈칸
        print("★ ",end="")
    print('')
    for j in range(6-i): #빈칸
        print("  ",end="")
    for j in range(0,3+i*2,1):
        print("☆ ",end="")
    print('')
        