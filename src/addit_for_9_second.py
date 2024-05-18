def count_words(filename: str) -> dict:
    """ Подсчитывает количество слов в файле.
        Возвращает словарь, содержащий количество каждого слова в файле.
    """

    word_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count


def list_of_words_in_file():
    """Функция принимает на вход название файла и возвр-ет строки
    "ключ-значение" из словаря с кол-вом слов в файле и самими словами"""
    filename: str = "example.txt"
    word_count: dict = count_words(filename)

    for word in word_count:
        print(word, word_count[word])

