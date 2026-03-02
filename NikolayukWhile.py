#HT_6_1
sum_1 = 0
num_1 = 0
num_1 = int(input())
while num_1!=0:
    if num_1 % 5 == 0:
        sum_1 += num_1
    num_1 = int(input())
print(sum_1)
#HT_6_2
plus = 0
minus = 0
num_1 = int(input())
while num_1!=0:
    if num_1 >= 0:
        plus += 1
    else:
        minus += 1
    num_1 = int(input())
print(f'Положительных: {plus}, отрицательных: {minus}')
#HT_6_3
num_1 = int(input())
div = 2
while div <= num_1//2 + 1:
    if num_1 % div == 0:
        print(f'Число {num_1} не простое')
        break
    div += 1
else:
    print(f'Число {num_1} простое')
#HT_6_4
zp = 0
num_1 = 0
num_1 = abs(int(input()))
while zp-num_1 > 0:
    zp-=num_1
    num_1 = abs(int(input()))
else:
    print(f'Стоп, Джон! Осталось {zp} денег')
#HT_6_4
#Чтобы стать профессионалом нужно заниматься делом 10000 часов
#Написать программу, которая будет принимать на вход число часов в день от пользователя, и рассчитывать через сколько лет он станет профессионалом в своем деле
#Программа не должна завершаться до того, как пользователь введет "Хватит"
promt = 'Сколько часов в день будем заниматься? Для выхода введите "Хватит"'
str_1 = str()
hours = 1
str_1 = input(promt)
while str_1 != 'Хватит':
    if str_1.isdigit():
        hours = int(str_1)
        print(f'Становление профессионалом через {(10000/(hours*365))} лет')
    else: print('Введено не число')
    str_1 = input(promt)