import numpy as np


size = int(input('Enter the size of the matrix from 1 to 100:'))

while (size < 1) or (size > 100):
    size = int(input("Oops, wrong size. Please, try again. " "\nEnter the size of the matrix from 1 to 100:"))

t = int(input('Enter the accuracy:'))
x = np.random.randint(10, size=(size, size)) # Задаём матрицу
rank = np.linalg.matrix_rank(x)              # Вычисляем ранг

print("Matrix:\n", x)
print("It's rank:", rank)

n = 1
cond, factorial, number_factorial = 1, 1, 1  # Задаём условие точности и факториал
sum, befsum = 0, 0                           # Задаём сумму и "бывшую" сумму

while abs(cond) > (0.1 ** t):                # Пока модуль разницы "бывшей" суммы и суммы больше точности, крутимся в цикле
    befsum += sum
    number_factorial = 2 * n + 1             
    factorial *= 2 * n * (2 * n + 1)         # Вычисляем факториал (2n+1) члена последовательности
    sum += np.linalg.det(x * number_factorial) / factorial
    n += 1
    cond = abs(befsum-sum)
    befsum = 0

print('Sum is:', sum)                        #Выводим сумму
