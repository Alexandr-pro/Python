# Задача 3.

print('Введите номер билета: ')
x = int (input())
d6 = x % 10
d5 = x // 10 % 10
d4 = x // 100 % 10
d3 = x // 1000 % 10
d2 = x // 10000 % 10
d1 = x // 100000 % 10

if d1 + d2 + d3 == d4 + d5 + d6:
    print('YES')
else:
    print('NO')