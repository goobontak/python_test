ProgarmLanguage= ["c언어","java","python","script"]
print(ProgarmLanguage)

ProgarmLanguage.pop() #set 속성 맨뒤삭제
print(ProgarmLanguage)

del ProgarmLanguage[1]
print(ProgarmLanguage)

del ProgarmLanguage[ProgarmLanguage.index("c언어")]
print(ProgarmLanguage)

ProgarmBook = ['언어길잡이','java시작']
a= ProgarmLanguage + ProgarmBook
print(a) 
ProgarmBook.extend(ProgarmLanguage) #합치기
print(ProgarmBook)
ProgarmBook.clear
print(ProgarmBook)
