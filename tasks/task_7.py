# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
number: int = int(input('Введите число:'))
divisor: int = 2
new_divisor: list = []

while divisor * divisor <= number:
    if number % divisor == 0:
        number //= divisor
        new_divisor += [divisor]
    else:
        divisor += 1

print(*new_divisor, sep=" ")
