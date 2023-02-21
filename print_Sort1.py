ar_num = [6,2,7,9,1,3]
print("정렬전 : " ,ar_num)
ar_num_desc = ar_num
print("정렬전 : " ,ar_num_desc)
ar_num_reverse = ar_num
print("정렬전 : " ,ar_num_reverse)
ar_str = ["banana","파인애플","pineapple","수박",130]
print()

ar_num_reverse.reverse() # list 뒤집기
print("정렬후1 : " ,ar_num_reverse)

ar_num.sort() #오름차순
print("정렬후2 : " ,ar_num)

print("정렬후 : " ,ar_num_reverse)

ar_num_desc.sort(reverse=True) #내림차순
print("정렬후 : " ,ar_num_desc)
ar_num_reverse.reverse() # list 뒤집기
print("정렬후3 : " ,ar_num_reverse)
ar_num_reverse.reverse() # list 뒤집기
print("정렬후3 : " ,ar_num_reverse)