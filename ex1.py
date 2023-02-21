my = input().split()
my1=[1,2,3,4]

my = list(map(int,my))

my2= list(set(my)-set(my1))


print(my2)
print(type(my2))

if len(my2)==1:
    print("굿")
if len(my2)==2:
    print("굿")
if len(my2)==3:
    print("굿")
if len(my2)==4:
    print("굿")
    
