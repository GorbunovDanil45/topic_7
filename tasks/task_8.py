# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
start: int = int(input('Введите начало диапазона:'))
finish: int = int(input('Введите конец диапазона:'))

if start > finish:
    start, finish = finish, start

if start % 2 != 0:
    start += 1

for i in range(start, finish + 1, 2):
    print(i)
