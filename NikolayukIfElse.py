# HT_4_1
# number = input()
number = -34
if float(number) >= 0:
    print('Положительное')
else:
    print("Отрицательное")

# HT_4_2 (°C × 9/5) + 32 = °F
# number = input()
# deg = input()
number = -34
deg = 'С'
if str(deg)[:1].upper() == 'С':
    print(float(number) * (9 / 5) + 32)
else:
    print((float(number) - 32) / (9 / 5))

# HT_4_3
# number1 = float(input())
# number2 = float(input())
# action = input()
number1 = float(2)
number2 = float(5)
action = '%'
if action == '+':
    print(number1 + number2)
elif action == '-':
    print(number1 - number2)
elif action == '*':
    print(number1 * number2)
elif action == '/':
    print(number1 / number2)
else:
    print('Не правильное действие')

# HT_4_4
# word_1 = input()
# word_2 = input()
word_1 = '123'
word_2 = '312'
if sorted(word_1) == sorted(word_2):
    print('anagram')
else:
    print('just words')

# HT_4_5 Приходит номер телефон. Опеределить из Беларуси он или нет (+375)
number = input('Введите номер телефона с кодом: ')
if number[:4] == '+375':
    print('Свои, всё норм')
else:
    print('Возмодно мошенники!')
