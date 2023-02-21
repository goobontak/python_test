a = 1000000
b = 100
c = 3.1425
print("{0:,d}".format(a))  # , 천단위 콤마
print("{0:7,d}".format(b)) # 7,d 7자리의 천단위 콤마 정수
print("{0:7d}".format(b))  # 7d 7자리의 정수
print("{0:.3f}".format(c)) # 실수 3자리까지 반올림