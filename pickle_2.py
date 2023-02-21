import pickle

menu_file = open("coffee_menu.txt","rb")
menu=pickle.load(menu_file)
print(menu)
menu_file.close()