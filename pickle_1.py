# 저장하기 : pickle.dump(변수(객체),파일)
# 불러오기 : pickle.load(파일)

import pickle
coffee_file = open("coffee_menu.txt","wb") # pickle은 2진수필요(b,바이너리)
menu = {"메뉴" : "아메리카노","가격" : 1500, "종류" : "hot", "옵션" : ["1샷추가","1시럽","얼음1알"]}
print(menu)
pickle.dump(menu,coffee_file)
coffee_file.close()