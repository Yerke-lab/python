#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]

#фильтруем список, используя метод enumerate находим числа на нечетных позициях
filtered = [x for i, x in enumerate(lst) if i % 2 != 0]

s = sum(filtered)
print(s)   
