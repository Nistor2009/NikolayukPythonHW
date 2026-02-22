# типы данных: int, float, complex, str
#           , _ - служебная переменная. хранит последнее вычисленное значение
# операции: +, -, *, /, // - деление без остатка(-4.5 получится -5), % - остаток от деления
#           , ** - возведение в степень. чтобы взять корень нужно использовать (1/3). Работает с права на лево.
# math: abs(-5), min(51,32,1,0,-9), max(3,1,2), pow(3,2) - степень, round(7.1258, 2) - округление
# str: len('str'), str(1), str_1[0], str_1[0:2], str_1[::-1] - выведет строку в обратном порядке
#       , str_1.find('1'), str_1.rfind('1'), str_1.index('1'), str_1.rindex('1') - вернёт индекс с 0. index вернёт ошибку если не найдет
#       , str_2 in str_1 - вернет true/false, str_1.replace(old, new, count), split(sep, count)
#       , f'str {name}' - форматирование, str_1.lstrip(), str_1.rstrip(), str_1.strip()
#       , str_1.isdigit(), str_1.isalpha(), str_1.isalnum(), str_1.isupper(), str_1.islower(), str_1.upper(), str_1.lower(). str_1.capitalize()
#       , ', '.join(str_1) - 'a, b, c, d', str_1.center(15), 'is cool' - поставит str_1 в центр из 15, str_1.count(str_2, start, end)
#     !!!, ord('A') - номер символа ASCII
# console help() -> keywords
# ввод с консоли: name = input() или name = input().split() - получим массив
a = 7
var_a = "hello"
b = a
a = b = c = 0
a, b = 6.7, 2
a, b = b, a #обмен значениями
print(a)
print(type(a))
print(id(a))


####################################
a+=1
print(a)
import math
print(math.ceil(a))


