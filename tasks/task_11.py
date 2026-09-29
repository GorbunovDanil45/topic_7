# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
rows: int = int(input('Введите целое положительное число:'))

for i in range(rows):
    for j in range(i + 1):
        print(i + 1, end=' ')
    print()

num: int = 0
while num <= rows:
    