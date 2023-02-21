num = [1,2,3,4,5,6,7,8,9,10]
print(num)

num10 = [i*7 for i in num]
print(num10)

city = {'Suwon','Wonju','Sokcho','Seoul'}
print(city)
city_len = [len(i) for i in city]
print(city_len)
city_swap = [i.swapcase() for i in city] # 대-> 소 / 소->대
print(city_swap)

