# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
number: int = int(input('Введите целое число:'))
absolute_value = abs(number)

if absolute_value == 0:
        count = 1

else:
    count: int = 0
    while absolute_value != 0:
        new_num = absolute_value % 10
        absolute_value = absolute_value // 10
        count += 1

print(f"Количество цифр в числе: {count}")
