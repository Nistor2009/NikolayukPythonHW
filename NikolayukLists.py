#HT_3_1
list_1 = list()
#list_1 = input().split()
list_1.reverse()
print(list_1)

#HT_3_2
list_1 = list(range(0, 11))
list_2 = [min(list_1), max(list_1), sum(list_1)]
print(list_2)

#HT_3_3
str_1 = 'ade rg gt5 re u'
# str_1 = input()
str_1 = str_1.replace(" ", "*")
print(str_1.count('*'))

#HT_3_4
#Получить на вход строку. Вернуть строку, состоящую из входящей с заглавной буквы, которая с половины длины будет идти в заглавном регистре в обратном порядке
str_1 = 'мама мыла раму'
# str_1 = input()
print(str_1.capitalize()[:int(len(str_1)/2)] + str_1[int(len(str_1)/2):].upper()[::-1])

#HT_3_5
#На вход подается строка. Вернуть список, состоящий из слов строки в обратном порядке, повторённых дважды
str_1 = 'мама мыла раму'
# str_1 = input()
list_1 = str_1.split(' ')
list_1.reverse()
list_1 = list_1 * 2
print(list_1)