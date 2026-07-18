number: int = int(input())
print(f"Таблица умножения для числа {number} с помощью цикла for:")

for i in range (1, 11, 1):
    result = number * i
    print(f"{number} * {i} = {result}")


print(f"Таблица умножения для числа {number} с помощью цикла while:")
j: int = 0
while j < 10:
    j += 1
    result_2 = number * j
    print(f"{number} * {j} = {result_2}")
