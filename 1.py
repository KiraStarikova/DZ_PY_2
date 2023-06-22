#Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

print('Введите целое число: ')
num = int(input())
print(hex(num))
numericStr = '0123456789ABCDEF'
res = ''
while num > 0:
    res = str(numericStr[num % 16]) + res
    num = num // 16
print(res)

