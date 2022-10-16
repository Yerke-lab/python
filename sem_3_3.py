# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
from this import d
lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst)
lst2 = [math.floor(v) for v in lst] # округляем элементы до целых чисел (отделяем от дробных частей) 

dif = []   
zip_object = zip(lst, lst2)
for lst_i, lst2_i in zip_object:
    dif.append(lst_i-lst2_i) # определяем дробные части элементов
dif = [i for i in dif if i != 0] # удаляем элементы равные нулю 

for i in str(dif):
    max_i = max(dif) # находим максимальное значение дробной части
    min_i = min(dif)
    min_i != 0 # находим минимальное значение дробной части
    fin = max_i - min_i # определяем разницу значений дробных частей
print('Максимальное значение дробной части', round(max_i, 3))
print('Минимальное значение дробной части', round(min_i, 3))
print('Разница между максимальной и минимальной дробных частей', round(fin, 3))