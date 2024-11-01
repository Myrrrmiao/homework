from array import array

n = int(input("Enter the number: "))
array = [] #массив в который будем потом закидывать простые числа

for i in range (2, n + 1): # берём и пробегаемся по заданному диапазону
    is_prime = True # создали переменную чтобы чекать является ли число простым
    for j in range (2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        array.append(i)

print(sum(array))
