"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_func(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(time.time() - start_time)
        return res
    return wrapped


@time_func
def add_dct(a, n):
    for i in range(n):
        dct[i] = i  # O(1)
    return a


@time_func
def add_lst(a, n):
    for i in range(n):
        lst.append(i)   # O(1)
    return a


@time_func
def pop_dct(a, n):
    for i in range(0, n, 5):
        dct.pop(i)  # O(1)
    return a


@time_func
def pop_lst(a, n):
    for i in range(0, n, 5):
        lst.pop(i)  # O(n)
    return a


dct = {}
lst = []
add_n = 100000000
pop_n = 1000

print(add_dct('add_dct', add_n))
print()
print(add_lst('add_lst', add_n))
print()
print(pop_dct('pop_dct', pop_n))
print()
print(pop_lst('pop_lst', pop_n))

# судя по замерам наполнение списка быстрее чем словаря,
# а вот работа с ним наоборот
