#HT_8_1
person = {
    'name': 'Вася',
    'age': 10,
    'city': 'Минск'
}
print(person['age'])
#HT_8_2
list_words = []
list_words = input().split()
dict_words = {}
for word in list_words:
    dict_words[word] = len(word)
print(dict_words)
#HT_8_3
list_numbers = []
dict_numbers = {}
list_numbers = [int(num_1) for num_1 in input().split()]
dict_numbers = {int(num_1) : int(num_1 * 1.1) for num_1 in list_numbers}
print(dict_numbers)
#HT_8_4
cars = {
    'BMW': [1,2,3]
    , 'Tesla': [4,5,6]
}
for key, value in cars.items():
    print(f'{key}: первое - {value[0]}, последнее - {value[len(value)-1]}')
#HT_8_5
#Вывести значения и ключи предыдущего словаря одним отсортированным списком. Сначала числа, затем строки
list_1 = []
for key, value in cars.items():
    list_1.append(key)
    [list_1.append(i) for i in value]
list_1.sort(key=str)
print(list_1)
#HT_8_6
dict_countries = {
    "Россия":"Москва"
    , "Украина":"Киев"
    , "Италия":"Рим"
    , "Испания":"Мадрид"
    , "Болгария":"София"
}
country = input("Столицу какой страны хотите узнать? ")
print(f"Ответ: {dict_countries[country]}")
#HT_8_7
dict_numbers = {
    1:"Один"
    , 2: "Два"
    , 3: "Три"
    , 4: "Четыре"
    , 5: "Пять"
}
dict_numbers = {key:value for key, value in dict_numbers.items() if key%2 != 0}
print(dict_numbers)
#HT_8_8
#Используя словарь стран преобразовать value к значению key имеет столицу value
for key, value in dict_countries.items():
    dict_countries[key] = f"{str(key)} имеет столицу {value}"
print(dict_countries)