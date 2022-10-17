#Напишите программу, которая найдёт произведение пар 
# чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import random 

n = int(input('Задайте длину списка: '))
lst = []
for i in range(n):
    num = random.randint(1, 10)
    lst.append(num)
print(lst)

lst2 = []
for i in range(len(lst)):
    if i < (n - 1) // 2 + 1:
        c = lst[i] * lst[len(lst)-i-1]
        i += 1
        lst2.append(c)
   
print('->', lst2)

