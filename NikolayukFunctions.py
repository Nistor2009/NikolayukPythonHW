#HT_13_1
import random


def sorted_num_sum(*args) ->list[int]:
    list_result = []
    for arg in args:
        list_result.append(sum([int(i) for i in str(arg)]))
    return sorted(list_result)

#HT_13_2
def func_x(x:float) -> float:
    def les_minus_2(x:float) -> float:
        return float(1 - (x + 2)**2)
    def between_2(x:float) -> float:
        return float((-1) * x / 2)
    def more_2(x:float) -> float:
        return float((x - 2)**2 + 1)
    if x <= -2:
        return les_minus_2(x)
    elif x > 2:
        return more_2(x)
    else:
        return between_2(x)

#HT_13_3
def devide_even_num(*args) ->list[int]:
    list_result = []
    for arg in args:
        if arg % 2 == 0:
            list_result.append(arg//2)
    return list_result

#HT_13_4
def get_random_list(count: int, min_num:int, max_num:int) -> list[int]:
    result = []
    for i in range(count+1):
        result.append(random.randint(min_num, max_num))
    return result

#HT_13_6
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)


print(sorted_num_sum(965, 582, '023', 8, 695210))
print(func_x(4.5))
print(devide_even_num(852, 85, 784, 58))
print(get_random_list(10, 2, 10))
print(factorial(5))