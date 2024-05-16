# Напишите функцию, которая принимает на вход список строк и возвращает
# список строк, в которых первая и последняя буквы совпадают. Если список
# пустой, верните пустой список.


def get_similar_char(my_list: list) -> list:
    """Ф-ия выводит новый список из слов, в которых 1-й символ = посл."""
    new_list: list = []

    if not my_list:  # если исходный список пустой, выводим пустой список
        new_list = []

    for i in my_list:
        if i[0] == i[-1]:
            new_list.append(i)
    return new_list


# Напишите ф-ию, кот. принимает на вход список целых чисел и возвращает макс.
# произв-ие 2-х чисел из списка. Если в списке менее 2-х чисел, ф-ия вернет 0.


def get_max_product(number_list: list) -> int:
    """Функция возвращает макс. произведение 2-х чисел из данного списка"""
    max_product: int = 1
    nmr_index: int = 1

    if len(number_list) < 2:  # если в сп-ке меньше 2-х эл-ов, возв-ем 0
        max_product = 0

    for i in number_list:
        for j in range(nmr_index, len(number_list)):
            if i * number_list[j] > max_product:
                max_product = i * number_list[j]
        nmr_index += 1
    return max_product