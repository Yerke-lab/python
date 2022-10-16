#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21].

def fib(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)
lst = []
for e in range(0, 9):
    lst.append(fib(e))

f2 = lst[:]
f2.reverse()
del f2[-1]
f2[0] = -f2[0]
f2[2] = -f2[2]
f2[4] = -f2[4]
f2[6] = -f2[6]
lst = f2 + lst
print(lst)