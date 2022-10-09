#Задайте список из N элементов, заполненных
# числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.


with open('1file.txt', 'r') as my_file: #считываем данные из текстового файла
    data = my_file.read()
lst = data.split()

int_lst = [int(x) for x in lst] # Преобразуем список строековых чисел в список целых чисел
print (int_lst)

multiply = 1
for i in int_lst:
    multiply *= i
print(multiply)

