
def func2(num1,num2):
    s=10
    s =s+ num1 + num2
    print(num1)
    print(num2)
    print(s)
    return s 

def func1():
    for i in range(0,2):
        print('function')
        if i==1:
            print('iiiii')
func1()

   


def func3(a,b):
    x = a*b
    print(x)
    return x
print(func3(9,7))


func2(10,5)