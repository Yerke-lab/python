# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#и проверяет, является ли этот день выходным.; Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

print('Введите день недели: ')
n = int(input())
if 8 > n > 5:
    print(n, ' -> да')
elif n < 6:
    print(n, ' -> нет')
else:
    print('Вы ввели некорректно день недели. Попробуйте заново')