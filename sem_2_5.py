#Реализуйте алгоритм перемешивания списка.

import random 

n = int(input('Задайте длину списка: '))
lst = []
for i in range(n):
    num = random.randint(1, 100)
    lst.append(num)
print(lst)
random.shuffle(lst) #функция случайного перемешивания массива
print(lst)

