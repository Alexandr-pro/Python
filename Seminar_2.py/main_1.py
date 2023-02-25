# Задача 10.
#  На столе лежат n монеток. 
#  Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите число монеток: '))
from random import randint
list_coins = []
for i in range(n):
    list_coins.append(randint(0, 1))
print(list_coins)
zero = list_coins.count(0)
if len(list_coins) - zero < zero:
    print(f'Нужно перевернуть {len(list_coins) - zero} монеток')
else:
    print(f'Нужно перевернуть {zero} монеток')