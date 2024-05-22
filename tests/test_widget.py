from src.widget import get_date, mask_for_acc_card


def test_mask_for_acc_card():
    str_new: str = "Visa Gold 8976700079228958"
    assert mask_for_acc_card(str_new) == 'Карта Visa Gold 8976 70** **** 8958'
    assert mask_for_acc_card('') == ''


def test_get_date():
    date_for_ex: str = '2018-12-11T02:26:18.671407'
    assert get_date(date_for_ex) == '11.12.18'
    assert get_date('') == ''
    assert get_date([]) == ''
    assert get_date({}) == ''
