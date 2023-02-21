su =int(input('피보나치 입력 : '))
num=[0]

a=1
su1=0
su2=1
print(a,end='')
for i in range(1,su):
    su3=su1+su2
    print('+',su3,end='')
    su1=su2
    su2=su3
    
    
