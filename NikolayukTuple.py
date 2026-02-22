# HT_7_1
import random
list_1 = list(range(10))
list_2 = list(range(10))
for i in range(10):
    list_1[i] = random.randint(-5, 0)
    list_2[i] = random.randint(-5, 0)
tp1 = tuple(list_1)
tp2 = tuple(list_2)
tp3 = tp1 + tp2
print(tp3.count(0))

# HT_7_2
list_1 = list(range(5))
for i in range(5):
    list_1[i] = random.randint(1, 10)
tp1 = tuple(list_1)
print(tp1)
first, *list_2, last = tp1
print(list_2)

# HT_7_3
# list_1 = list(input().split())
list_1 = [1, 4, 5, 6, 3, 7]
list_2 = list(range(len(list_1)))
list_2.clear()
for i in range(len(list_1)):
    if int(list_1[i]) < 5:
        list_2.append(int(list_1[i]))
tp1 = tuple(list_2)
print(tp1)

# HT_7_4
tp1 = (1, 4, [3,4,5], 'tgt')
tp1[2].clear()
print(tp1)

# HT_7_5 Создать кортеж из списка чтобы он состоял только из строк(всё остальное не брать). Результат вывести одной строкой
list_1 = [1,3, 'Привет', 5/6, 12, ' ', 3,6, 'медвед', 5*2, 11]
list_2 = list(range(len(list_1)))
list_2.clear()
for i in range(len(list_1)):
    if type(list_1[i])==type('str'):
        list_2.append(list_1[i])
tp1 = tuple(list_2)
str_1 = ''
str_2 = ''
for i in range(len(tp1)):
    str_1 = str_1 + str(tp1[i])
print(str_1)