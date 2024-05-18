from src.addit_for_9_second import count_words, list_of_words_in_file
from src.addit_for_10_first import list_sort_prod_price, quant_avg_pr_month

import os

#делаем вызов функции подсчета слов в файле
file_name = 'example.txt'
print(count_words(file_name))
print(list_of_words_in_file())

# назначаем переменные для работы функций из модуля 10_first
# для функции сортировки по цене... (list_of_words_in_file())

list_orig: list = [
    {"name": "Cola", "price": 234, "category": "food", "quantity": 12},
    {"name": "Copybook", "price": 34, "category": "stationery", "quantity": 345},
    {"name": "Pencil", "price": 124, "category": "stationery", "quantity": 4},
    {"name": "Eggs", "price": 567, "category": "food", "quantity": 5},
    {"name": "Hammer", "price": 4567, "category": "tools", "quantity": 6}
]

# и для функции сортировки по категориями (quant_avg_pr_month())

list_dict: list = [
{'id': 344, 'date': '12-11-2018', 'items': {'name': 'glass', 'price': 231, 'quantity': 101}},
{'id': 342, 'date': '13-11-2018', 'items': {'name': 'cup', 'price': 234, 'quantity': 245}},
{'id': 345, 'date': '14-12-2018', 'items': {'name': 'pencil', 'price': 44, 'quantity': 5015}},
{'id': 346, 'date': '13-12-2018', 'items': {'name': 'table', 'price': 2345, 'quantity': 17}},
{'id': 347, 'date': '05-01-2019', 'items': {'name': 'hammer', 'price': 1717, 'quantity': 9}},
{'id': 348, 'date': '07-01-2019', 'items': {'name': 'saw', 'price': 1010, 'quantity': 11}}
]

# и вызываем эти функции

print(list_sort_prod_price(list_orig))
print(quant_avg_pr_month(list_dict))





