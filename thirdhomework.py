'''
Задача 1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
Пример:
[1, 2, 3, 1, 2, 4, 5] -> [1, 2]
'''
list_num = [1, 2, 3, 1, 2, 4, 5]
result = []
number = 0
for number in list_num:
    if list_num.count(number) > 1:
        result.append(number)
result_dubl = list(set(result))
print(result_dubl)

'''
Задача 2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или 
из документации к языку.
'''
big_str = '''Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.
This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.
For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.
'''

big_str = big_str.lower()
big_str = big_str.replace('.', ' ')
big_str = big_str.replace(',', ' ')
big_str = big_str.replace('(', ' ')
big_str = big_str.replace(')', ' ')
big_lst = big_str.split()

count = {}
for word in big_lst:
    if count.get(word, None):
        count[word] += 1
    else:
        count[word] = 1

sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
count_word = dict(sorted_values)
count_word_keys = list(dict.keys(count_word))
for i in count_word_keys[:10]:
    print(i)

'''
Дополнительно:
Задача 1:
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
Верните все возможные варианты комплектации рюкзака.
'''
backpack = {'canned_food': 3, 'flashlight': 1, 'tent': 5, 'beer': 3, 'knife': 1, 'axe': 2}
BAGGAGE = 12
ves = BAGGAGE
sorted_things = dict(sorted(backpack.items(), key=lambda x: -x[1]))
for k, v in sorted_things.items():
    if v > ves:
        continue
    if v <= ves:
        print(k, sep='/n')
    ves -= v

'''
Дополнительно:
Задача 2:
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:
** какие вещи взяли все три друга
** какие вещи уникальны, есть только у одного друга
** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей. 
(часть уже сделана на семинаре и лежит на гите https://github.com/bettercallvlad/deep_sem3)
'''
baggage = {
    'Denis': ('fishing rod', 'lighter', 'tent'),
    'Alex': ('tent', 'brazier', 'gun'),
    'Vlad': ('tent', 'gun', 'sun cream')
}
all_items = list(baggage.values())
must_have_item = set(all_items[0])
for items in all_items:
    must_have_item = must_have_item.intersection(set(items))
print(must_have_item)

uniq_item_list = []
for bagg_name, bagg_items in baggage.items():
    other_friend = set()
    for other_friend_name, other_friend_items in baggage.items():
        if other_friend_name == bagg_name:
            continue
        other = other_friend.union(set(other_friend_items))

    uniq_item_list.append((set(bagg_items) - other_friend, bagg_name))

for thing, name, in uniq_item_list:
    print(f'У {name} уникальная вещь {thing}')

absent = []
for bagg_name, bagg_items in baggage.items():
    temp_items = set()
    for other_friend_name, other_friend_items in baggage.items():
        if other_friend_name == bagg_name:
            continue
        elif not temp_items:
            temp_items = set(other_friend_items)
            continue

        if temp_items != other_friend_items:
            other = temp_items.intersection(set(other_friend_items))
            temp_items = other_friend

    absent_items = other_friend - set(bagg_items)
    if absent_items:
        absent.append((absent_items, bagg_name))

for item, name in absent:
    print(f'{item} нет у {name}, но есть у остальных')
