# Удалить элемент с введенным номером

import random
n = int(input("Введите размер списка ="))
A = []
for i in range(n):
    a = random.randint(0,10)
    A.append(a)

for i in range(n):
    print(A[i])

k = int(input("Введите номер k="))
A.pop(k)
for i in range(n-1):
    print(A[i])