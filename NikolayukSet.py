# HT_9_1
# str_1 = input()
# str_2 = input()
str_1 = 'dsghdyjdxfvg'
str_2 = 'dsgiluikjsaetfvg'
set_1 = set(str_1)
set_2 = set(str_2)
print(set_1&set_2)

#HT_9_2
# str_1 = input()
# str_2 = input()
str_1 = 'ffrtasd'
str_2 = 'hhfsecb'
set_1 = set(str_1)
set_2 = set(str_2)
print(set_2-set_1)

#HT_9_2 Получить 2 строки. Объединить их уникальные символы и вывести в отсортированном виде
str_1 = input()
str_2 = input()
# str_1 = 'ffrtasd'
# str_2 = 'hhfsecb'
set_1 = set(str_1)
set_2 = set(str_2)
print(sorted(set_2|set_1))