kuk = int(input('국어점수 :'))
su= int(input('수학점수 :'))

if kuk>= 90 and su>= 90:
    print("두과목 90이상")
elif kuk>=90 or su>=90:
    print("한과목90이상")
else :
    print("모두90미만")

