# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
number: int = int(input('Введите число:'))

if number < 1:
    print('Число должно быть больше или равно 1')

elif number == 1:
    print('1')

else:
    count: int = 0
    result: int = 0
    while count < number:
        count += 1
        result += count

    print(f'Сумма всех чисел от 1 до {number} будет равна: {result}')