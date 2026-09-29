# Исходный список чисел
numbers = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

# TODO: Пожалуйста, добавьте свой код ниже с комментариями и понятными названиями переменных.
for element in numbers:
    number = int(element)
    if number > 100 and (number % 5 == 0 or number % 7 == 0):
        print(number, end=' ')
