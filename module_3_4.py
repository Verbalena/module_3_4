# Задача "Однокоренные"
def single_root_words(*other_words, root_words = 'мир'):
    same_words = []                       # создать пустой список
    for i in other_words:
        if root_words.lower() in i.lower():  # сравнить root_words с каждым элементом other_words без учета регистра
            same_words.append(i)             # добавить элемент в список

    return print(same_words)

rezalt_1 = single_root_words( 'мера', 'Мирный', 'миролюбие', 'мирить', 'измерение')
rezalt_2 = single_root_words('бездомный', 'Домовой', 'бездна', 'домашний', 'удалой', root_words = 'дом')
