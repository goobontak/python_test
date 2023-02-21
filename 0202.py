su_cnt , ar_cnt = map(int,input().split())
num = list(map(int,input().split()))
print(type(num))
sum_ar=[0]
temp = 0
for i in num:
    temp+=i
    sum_ar.append(temp)
start =[]
end=[]
for i in range(ar_cnt):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

for i in range(ar_cnt):
    print(sum_ar[end[i]]-sum_ar[start[i]-1])
  
  
'''
num_cnt = int(input('몇개의 숫자를 입력하시겠습니까? '))
num_in = list(map(int,input().split()))
print(num_in)



ar = [1,2,3,4,5]
s,e = map(int,input().split())
sum_ar = []
for x in range(s-1,e):
    sum_ar.append(ar[x])
print(sum(sum_ar))

'''
    