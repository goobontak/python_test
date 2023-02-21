import sys
ar = []
cnt = int(input('몇번 계산 하시겠습니까? ')) #map(int,input('몇번 계산 하시겠습니까? '))
for x in range(cnt):
    a, b = map(int,sys.stdin.readline().split())
    ar.append(a+b)
print(ar)
print(sum(ar))