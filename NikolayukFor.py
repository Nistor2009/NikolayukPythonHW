num_1 = 0
#HT_5_1
sum_1 = sum([i for i in range(1,11) if i%2==0])
print(sum_1)
#HT_5_2
num_1 = int(input());
for j in range(1, num_1 + 1):
    [print(i,end=" ") for i in range(1, j + 1)]
    print()
#HT_5_3
num_1 = [int(i) for i in input().split()]
for i in num_1:
    print('*' * i)
#HT_5_4
#5.4
num_1 = [int(i) for i in input().split()]
for i in range(min(num_1), max(num_1)+1):
    print(i, end=" ")
#5.5
num_1 = [int(i) for i in input().split()]
for i in range(min(num_1), max(num_1)+1):
    if i % 2 == 0:
        print(i, end=" ")
#5.7
num_1 = list(input())
[print(i*2, end='') for i in num_1]
#HT_5_5
# На вход приходит строка. Вывести сумму котов ASCII
num_1 = list(input())
print(sum([ord(i) for i in num_1]))