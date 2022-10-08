#Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

lst = []
for i in range(3):
    lst.append(int(input('Введите число: ')))
print(lst)
left = not (lst[0] or lst[1] or lst[2])
right = not lst[0] and not lst[1] and not lst[2]
result = left == right
if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')