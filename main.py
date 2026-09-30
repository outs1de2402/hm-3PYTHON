""" age  = int(input())
if age < 12:
    print("Дитина")
elif 12 <= age <= 17 :
    print("Підліток")
else:
    print("Дорослий") """




""" a  = int(input())
if a % 2 == 0:
    print("Парне")
else:
    print("Непарне") """


""" a = int(input())
b = int(input())
if a == b:
    print("Числа рівні")
else: 
    print(max(a, b)) """


""" price = int(input("Сума покупки: "))
if price < 1000:
    print("Сума знижки: 0, кінцева ціна: ", price)
elif 1000 <= price <= 5000:
    procent = (5 * price) / 100
    print(f"Сума знижки: {procent}, кінцева ціна: {price - procent}")
else:
    procent = (10 * price) / 100
    print(f"Сума знижки: {procent}, кінцева ціна: {price - procent}")
 """


""" mark = int(input("Кількість балів: "))
if mark >= 90:
    print("Відмінно")
elif mark >= 75:
    print("Добре")
elif mark >= 60:
    print("Задовільно")
else:
    print("Незадовільно")

 """


""" 
a = int(input())
b = int(input())
c = input("Виберіть дію: + - / *: ")
if c == '+':
    print(a + b)
elif c =="-":
    print(a-b)
elif c == "/":
    if b == 0:
        print("На нуль ділити не можна")
    else:
        (a / b)
elif c == "*":
    print(a * b)
else:
    print("Нема такої операції")  """




""" y = int(input("Який рік вас цікавить?: "))
if (y % 400 == 0 or y % 4 == 0) and y % 100 != 0:
    print("Високосний")
else:
    print("Не високосний") """


""" a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("Трикутник існує")
else:
    print("Трикутник з такими вимірами існувати не може") """



""" m = int(input())
if m == 12 or m == 1 or m == 2:
    print("Зима")
elif m == 3 or m == 4 or m == 5:
    print("Весна")
elif m == 6 or m == 7 or m == 8:
    print("Літо")
elif m == 9 or m == 10 or m == 11:
    print("осінь") """

""" a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c) """

""" a = 1
while a <= 10:
    print(a)
    a +=1 """

""" a = int(input("Введіть число "))
b = 1
while b <= a:
    b += 1
sum  = (a * (a+1)) / 2
print(sum) """


""" a = 2
while a <= 20 and a % 2 == 0:
    print(a)
    a += 2 """


""" n = int(input())
b = 1
factr = 1 
while b <= n:
    factr *= b
    b += 1
print(factr) """


""" n = int(input())

while n >=1 :
    print(n)
    n -= 1
 """



""" secret_number = 42 
a = 1
while a <= 7:
    b = int(input())
    if b == secret_number:
        print("Вітаємо! Це було число: ", secret_number)
        break;
    elif b >= secret_number:
        print("Менше ")
    elif b <= secret_number:
        print("Більше ")
    else:
        print("Виникла помилка")
    a +=1 """


""" sum = 0
count = 1
while sum <= 100:
    a = int(input())
    sum += a
    count += 1
print(sum, count - 1) """

""" num = 2 
while num <= 1000:
    print(num)
    num *= 2 """


""" while True:
    a = int(input())
    if 1 <= a <= 10:
        print("Дякую")
        break """


""" a = int(input("Введіть число для якого хочете отримати таблицю множення: "))
count = 1 
while count <= 10:
    print(count * a)
    count += 1 """



""" for i in range(1, 21):
    print(i) """


""" a = int(input())
b = int(input())
total  = 0
for i in range(a, b + 1):
    total += i
print(total) """


""" n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i) """


""" text = "Python"
for i in range(len(text)):
    print(f"{i}: {text[i]}")
 """


""" t = str(input("Введіть свій текст: "))
g = "aeiou"
c = 0
for i in t.lower():
    if i in g:
        c += 1
print(c) """


""" 
for i in range(1, 16):
    res = i ** 2
    print(f"{i}² = {res}")  """

""" 
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 :
        print("FizzBuzz")
    else:
        print(i) """



""" a = int(input())
b = str(a)
for i in b[::-1]:
    print(i) """

""" n = int(input())
for i in range(1, n+1):
    print("*" * i) """


""" n = int(input())
c = 1
for i in range(1, n + 1):
    if i % 2 != 0 :
        c *= i
print(c)
 """
""" 
for i in range(1, 101):
    if i % 2 == 0 :
        print(i)
        break """

""" for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i) """



""" text = "Programming"

for i in range(len(text)):
    if text[i] != 'a':
        continue
    print(i + 1)
    break
else:
    print("Не знайдено") """




""" sum = 0 
for i in range(1, 101):
    sum += i
    if sum > 500:
        print(i)
        break
print(sum) """


""" for i in range(5):
    a = int(input())
    if a <= 0 :
        continue
    print(a) """


""" for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}") """



""" w = int(input())
h = int(input())
for i in range(w):
    for j in range(h):
        print("*", end=' ')
    print() """


""" n = int(input())
for i in range(1, n + 1):
    print("*" * i) """




""" n = int(input())
for i in range(n):
    for j in range(n - 1 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print() """




""" n = int(input())
for i in range(n):
    if i % 2 == 1:
        print(" ", end="")
    for j in range(n):
        print("#", end=" ")
    print() """



""" n = int(input())
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i) """


""" for i in range(100, 1000):
    if i // 100 == i % 10:
        print(i) """


""" n = int(input())
a = 0
b = 1
for i in range (n):
    print(a)
    c = a + b
    a = b
    b = c """


""" a = int(input())
b = int(input())
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a) """



""" n = int(input())
sum = 0 
for i in range(1, n):
    if n % i == 0:
        sum += 1
if sum == n:
    print('Досконале')
else:
    print("Недосконале") """


""" n = int(input())

while n >= 10:
    sum = 0 
    for i in str(n):
        u = int(i)
        sum += u
    n = sum
print(sum) """


""" import math as m 
n = int(input())

if n <= 1 or (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3):
    print("Число не є простим")
else:
    is_prime = True
    i = 5
    while m.sqrt(n) >= i:
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
        i += 6
    if is_prime:
        print("Просте")
    else:
        print("Не просте") """



""" n = int(input("Введіть число Армстроннга: "))
sum = 0
p = str(n)
for i in p:
    k = int(i) ** len(p)
    sum += k
if sum != n:
    print("Не є числом Армстронга")
else:
    print("Число Армстронга")
         """

""" n = int(input("непарне число: "))

for i in range(1, n+1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
    
for j in range(n - 2, 0, -2):
    spaces = (n - j) // 2
    print(" " * spaces + "*" * j) """




""" print("\tКалькулятор\n")
while True:
    print("1.Додавання")
    print("2.Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")
    n = int(input("Ваш вибір(1-5): "))
    if n == 5:
        break
    a = int(input("Введіть 1 число: "))
    b = int(input("Введіть 2 число: "))
    match n:
        case 1:
            res = a + b
            print(res)
        case 2:
            res = a - b
            print(res)
        case 3:
            res = a * b
            print(res)
        case 4:
            if b == 0:
                print("Помилка, на нуль ділити не можна!")
            else:
                res = a / b
                print(res) """