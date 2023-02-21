import tkinter

subway_1={"1호선": ["소요산", "동묘앞", "을지로입구", "노량진"], "2호선": ["시청", "을지로입구", "강남", "잠실"],    }

print(subway_1)



print(len(subway_1))


print(subway_1.get("1호선")[1])


my_key_value = subway_1["1호선"]
my_key_length = len(my_key_value)
print(my_key_length)