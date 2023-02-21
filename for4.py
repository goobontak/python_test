for i in range(1,10):
    su =[i*j for j in range(1,10)]
    for k in range(2,10):
        print("{0:2d} x {1:2d} = {2:2d}".format(k,i,su[k-1]),end=" ")
    print('\n')
    
    