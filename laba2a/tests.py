# виводимо константи
var_1 = Ellipsis
print(var_1)
var_2 = None
print(var_2, '\n')

# виводимо результат роботи простих функцій
# оскільки моє прізвище починається на букву О, демонструю виконання функції ord()
# ord() - повертає для вказаного Юнікод-символу ціле число, яке являється його позицією
letter = 'b'
a = ord(letter)
print("Позиція букви '{0}' в Юнікоді: ".format(letter), a, '\n')

b = list(range(1, 11, 1))
print(b)

print("Якщо до {0} додати {1} отримаємо {2}".format(1, 2, 3), '\n')

# використовуємо цикл та розгалуження
# цикл
for i in (1, 2, 3, 4, 5):
	print("i={0} i^2={1}".format(i, i**2))

# розгалуження
var_3 = int(input("\nВведіть число: "))
if var_3 >= 5:
	print("Введене число більше або дорівнює 5\n")
else:
	print("Введене число менше 5\n")

# конструкція try->except->finally
try:
	print("Спробуємо вийти за межі масиву.")
	ar = ['0', '1', '2']
	print(ar[5])
except IndexError:
	print("Помилка виходу індексу за межі масиву.")
finally:
	print("Ось такий результат.\n")

# відкриємо файл з допомогою контекст-менеджера with
with open("text_file.txt", 'r') as var_4:
	print(var_4.read())

# використовуємо в своєму коді lambda 
arr = list(range(1, 6, 1))
arr2 = list(map(lambda x: x*2, arr))
print(arr2, "\n")
