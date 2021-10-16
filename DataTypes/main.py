# это наш первый комментарий
var = 0


# --ВСЕГДА-- называть переменные значимым именем или тем, для она используется.
variable = 13   # переменная называется "variable"
counter = 20     # используется для того, чтобы что-то считать


# переменные в языке Python начинаються с прописной буквы. Все последующие слова пишуться слитно и с заглавной буквы.
# переменные --ВСЕГДА-- латиницей, на анлгийском языке.
blueCarIgor = ''


# Добавляйте текстовое описание перед выводом значений переменной для того, чтобы было легче читать вывод
# результата исполнения кода.
# print("Значение переменной counter: ", counter)
# print("hello %s I am %s" % (counter, variable))
# print("Hello, my \n name is \n Bolathan!")

#######################################################################################################################
# Задание 1: 0. Создать новый проект в PyCharm. Назвать его "LecProject1".
#            1. Создать переменные, которые будут содержать Ваши "ФИО", возраст, город рождения, группу.
#            2. Вывести на экран все значения в одну строку в формате "ФИО: ____, __ лет, из: ___, учится в группе: _".
#            3. Вывести на экран все значения (каждое на новой строке), но одной линией кода (использовать "\n" и только
#               один "print()").
#######################################################################################################################

# --ВАЖНО-- примитивные типы данных языка Python
x = 13                          # integer
#print(x)
#print(type(x))                 # выводит тип данных переменной

y = 1.2                         # floating point number
#print(y)
#print(type(y))

#print(y-1)                     # что пошло не так? где 1.2?

myString = 'myString value'     # последовательность символов
myString2 = "myString2 value"

#print('x*2 = ', x*2)
#print('y*x = ', y*x)
#print('myString * x = ', myString*x)

# будьте осторожны с типами вот в таких случаях
znachenie = '44'
#print(znachenie*3)

boolean = False
#print('значение boolean = ', boolean, '; тип переменной: ', type(boolean))


# --ВАЖНО-- встроенные типы данных языка Python
mySet = {13, 14, 16, 98, 13}    # множество - set
myTuple = (15, 46, 46, 48)      # кортеж - tuple
myList = [64, 7, 49, 64, 49]    # список - list

#print(mySet)
#print(myTuple)

# --МОЖНО-- преобразовать один тип в другой
с = set(myTuple)
#print(с)

r = tuple(с)
#print(r)


# --ВАЖНО-- арифметические операции
#print(x*y)                     # умножение
#print(x+y)                     # сложение
#print(x/y)                     # деление
#print(x-y)                     # вычитание


# методы списков
#print(myList)
#print(myList.count(7))      # взвращает количество объектов в списке

myList.append(88)           # добавляет элекмент в конец
#print(myList)

myList.insert(0, 55)        # вносит новый элекмент номер 0 со значением 55
#print(myList)

myList.remove(49)           # удяляет первое значение 49 в списке
#print(myList)

newList = [1, 21, 32]         # новый список newList со значениями 1, 2, 3
myList.extend(newList)        # добавляет значения списка newList в конец myList
#print(myList)

myList.clear()              # очищает список
#print(myList)

# методы меняют сам список
myList.extend(newList)
#print(myList)

#primerList = myList.extend(newList)
#print(primerList)

#print(myList)
#first = myList.pop(0)       # возвращает значение номер 0 и удаляет его
#print(first)
#print(myList)

#######################################################################################################################
#  Задание 2: 1. Попробуйте сохранить в список следующий вектор: [13, 46, 79, 85, 95].
#             2. Реализуйте умножение вектора из 1 на: 34.
#######################################################################################################################
vector = [13, 46, 79, 85, 95]
outputVector = []

value = vector.pop(0)
outputVector.append(value * 34)
print(outputVector)
print(vector)

value = vector.pop(0)
outputVector.append(value * 34)
print(outputVector)
print(vector)

value = vector.pop(0)
outputVector.append(value * 34)
print(outputVector)
print(vector)

value = vector.pop(0)
outputVector.append(value * 34)
print(outputVector)
print(vector)

value = vector.pop(0)
outputVector.append(value * 34)
print(outputVector)
print(vector)


# Итерационная конструкция for
cars = ['Mazda', 'Mers', 'Toyota', 'BMW']

for i in cars:
    print(i)
    print(i*3)

#######################################################################################################################
#  Задание 3: Переписать код Задания 2 с использованием конструкции for.
#######################################################################################################################


# Упражнение 1
#print('Упражнение 1. Введите глубину ёлки:')
#stars = int(input())

#for star in range(1, stars+1):
#    print(star * '*')

# Упражнение 2
# для упражнения 3: для языков С, С++ был вывод "Почти как Pyhton, тоже красивый".

#print('Упражнение 2. ')
languages = ["C", "Delphi", "Python", "C++", "HTML", "Perl"]

#for language in languages:
#    if language == 'Python':
#        print('Python очень крутой')
 #   else:
#        print(language, 'не так крут, как Python')

# Упражнение 3
#print('Упражнение 3. ')
#for language in languages:
#    if language == 'Python':
#        print(language, 'очень крутой')
#    elif (language == 'C') | (language == 'C++'):
#        print(language, 'почти как Pyhton, тоже красивый')
#    else:
#        print(language, 'не так крут, как Python')


myString = 'Hello World'
i = 0

#for character in myString:
#    if character == 'l':
#        print(character)
        # continue            # команда, которая запускает следующую итерацию
#        i = i+1
#    else:
#        print('not an L')

#print("#character:", i)

# Цикл while, используется тога, когда вы не знаете размера входных данных.
i = 0

#while -5 < i < 5:
#    print(i)
#    # continue
#    # break
#    i = i-1

# ДЗ: 1. Решение ёлочки (для тех, кто не решил на уроке) с применением while.
#     2. Переделать ёлочку так, чтобы минимальное значение для высоты было 3, а максимальное 30
#        (через логическое условие while).
#     3. Доработать ёлочку так, чтобы после вывода основной ёлочки, программа дорисовывала ей ножку тольщиной 2 зыезды
#        (**), глубиной 3 звезды.
