from datetime import datetime

# Функция прин-ет на вход строку с информацией о типе карты и счета и номер
# карты или счета и возвращает маску карты (счета) по шаблону
# карта: XXXX XX** **** XXXX; Счет: **XXXX


def mask_for_acc_card(work_str: str) -> str:
    """Функция возвращает маску для номера счета или карты по шаблону **XXXX и
    XXXX XX** **** XXXX соответственно, самостоятельно определяя, счет это или
    карта"""

    mask: str = ""

    if work_str[0:4] == "Счет":
        mask = "Счет " + "**" + work_str[21:25]
    else:
        for i in work_str:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                new_str = work_str[work_str.find(i): len(work_str)]
                mask = (
                        "Карта " + work_str[0: work_str.find(i)] + new_str[0:4] + " "
                    + new_str[4:6]
                    + "** **** "
                    + new_str[12:16]
                )
                break

    return mask


# Напишите функцию, которая принимает на вход строку вида
# 2018-07-11T02:26:18.671407  и возвращает строку с датой в виде 11.07.2018


def get_date(curr_date: str) -> str:

    date_interm = datetime.strptime(curr_date, "%Y-%m-%dT%H:%M:%S.%f")
    date_output = datetime.strftime(date_interm, "%d.%m.%y")

    return date_output
