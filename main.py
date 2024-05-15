from src.widget import get_date, mask_for_acc_card
from src.widget_addit import get_max_product, get_similar_char

# переменные для проверки основного задания
date_for_ex = "2018-12-11T02:26:18.671407"
str_new: str = "Visa Gold 89767000792289606361"

# переменные для проверки дополнительного задания
list_for_list_char: list = ["helloh", "worldw", "apple", "pear", "banana", "pop"]
list_for_product = [2, 3, 5, -7, 11, -345]

# вызываем фукнции из основного задания
print(f"Маскированныый номер сущности: {mask_for_acc_card(str_new)}")
print(f"Дата в формате ДД.ММ.ГГГГ: {get_date(date_for_ex)}")

print()
# вызываем функции из дополнительного задания
print(f"Нов. сп-к один. 1-й и посл. бкв.: {get_similar_char(list_for_list_char)}")
print(f"Макс. произв. эл-ов списка равно {get_max_product(list_for_product)}")
