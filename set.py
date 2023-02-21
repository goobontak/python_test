city_a={'seoul','wonju','suwon','sokcho'}
city_b=set(['deagu','busan','jeounju','dokdo'])

print("seoul" in city_a)
print("seoul" in city_b)

city_a.add("incheon") #1개
city_a.update(["mars","a-town"]) #2개이상 추가 ->[]로 해야 오류없음
print(city_a)

city_a.remove("seoul")
print(city_a)

print(city_a.union(city_b))
print(city_a)

python= '123'
