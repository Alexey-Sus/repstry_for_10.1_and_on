# посмотреть вот тут: https://bytegeek.ru/sortirovka-fajlov-v-direktorii-po-date-sozdaniya
# -ili-izmeneniya-v-python/


# Напишите ф-ю, кот. приним-ет на вход список словарей и возвр. новый список,
# в кот. исх. словари отсорт-ны по убыванию даты (ключ date). Принимает 2 арг-та: 2-й - необяз. поряд. сорт.

list_orig: list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELLED", "date": "2018-10-14T08:21:33.419441"},
]


def list_sort_date(work_list: list) -> list:
    return sorted(work_list, key=lambda x: x["date"], reverse=False)


for i in list_sort_date(list_orig):
    print(i)

# Напишите функцию, которая принимает на вход список словарей и значение для ключа
# state (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
# содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
print()


def list_for_state(work_list: list, state_val="EXECUTED") -> list:
    state_new: str = input("Enter the /state/ parameter (EXECUTED/CANCELLED): ").upper()
    list_new: list = []
    if state_new not in ["CANCELLED", "EXECUTED"]:
        state_val = "EXECUTED"
    else:
        state_val = state_new
    for i in work_list:
        if i["state"] == state_val:
            list_new.append(i)
    return list_new


for i in list_for_state(list_orig):
    print(i)
