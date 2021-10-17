# бұл  біздің алғашқы комментарий
var = 0


# --ӘРҚАШАН-- айнымалыларды мағыналы атау немесе ол үшін қолданылатын тақырыптарды атау.
variable = 13   # айнымалылар "variable" деп аталады
counter = 20     # бір нәрсені санау үшін қолданылады


# Python тіліндегі айнымалылар кішкентай әріптен басталады. Барлық кейінгі сөздер бірге және бас әріппен жазылады.
# айнымалылар --ӘРҚАШАН-- латын қарпімен, ағылшын тілінде жазылады.
blueCarIgor = ''


# Нәтижені оқуды жеңілдету үшін айнымалы мәндерді шығарар алдында мәтіндік сипаттаманы қосыңыз
# кодты орындау нәтижесі.
# print("counter айнымалысының мәні: ", counter)
# print("hello %s I am %s" % (counter, variable))
# print("Hello, my \n name is \n Bolathan!")

#######################################################################################################################
# 1 тапсырма: 0. PyCharm - да жаңа проект құрамыз. Проектіні "LecProject1" деп атаймыз.
#            1. Сіздің "аты-жөні", жас шамасы, туған қаласы, тобының атауы болатын айнымалыларды құру.
#            2. "Аты - жөні: ____, __ жас шамасы, университет: ___,  _: группасында оқиды" барлық айнымалылардың мәнін бір жолда орналасатын форматта экранға шығару.
#            3. Барлық мәндерді экранға шығару (әрқайсысы жаңа жолда болуы қажет), бірақ код бір жолда ғана жазылу қажет ("\n" қолдану және тек
#               бір ғана "print()" қолдану).
#######################################################################################################################

# --МАҢЫЗДЫ-- Python тілінің қарапайым деректер түрлері
x = 13                          # integer бүтін
#print(x)
#print(type(x))                 # айнымалының деректер типін шығару

y = 1.2                         # floating point number нақты
#print(y)
#print(type(y))

#print(y-1)                     # Не болып қалды, не өзгерді? Біздің 1.2 қайда кетті?

myString = 'myString value'     # таңбалар тізбегі
myString2 = "myString2 value"

#print('x*2 = ', x*2)
#print('y*x = ', y*x)
#print('myString * x = ', myString*x)

# мұндай жағдайларда типтерге абай болыңыз
znachenie = '44'
#print(znachenie*3)

boolean = False
#print('boolean мәні= ', boolean, '; айнымалының типі: ', type(boolean))


# --МАҢЫЗДЫ-- Python тілінде кіріктірілген деректер типтері
mySet = {13, 14, 16, 98, 13}    # тізбек(множество) - set
myTuple = (15, 46, 46, 48)      # кортеж - tuple
myList = [64, 7, 49, 64, 49]    # тізім - list

#print(mySet)
#print(myTuple)

# --БОЛАДЫ-- бір типті басқа типке айналдыру
с = set(myTuple)
#print(с)

r = tuple(с)
#print(r)


# --МАҢЫЗДЫ-- арифметикалық операция
#print(x*y)                     # көбейту
#print(x+y)                     # қосу
#print(x/y)                     # бөлу
#print(x-y)                     # азайту


# тізімге қолданылатын методтар
#print(myList)
#print(myList.count(7))      # тізімдегі объектілер санын қайтарады

myList.append(88)           # тізімнің соңына элемент қосу
#print(myList)

myList.insert(0, 55)        # тізімдегі 0 - ші элементтің мәнін 55 ретінде қосу
#print(myList)

myList.remove(49)           # тізімдегі бірінші 49 мәнін һ-өшіру
#print(myList)

newList = [1, 21, 32]         # жаңа newList тізімінің мәндері 1, 2, 3
myList.extend(newList)        # myList тізіміне newList тізімінің мәндерін қосу
#print(myList)

myList.clear()              # тізімді тазарту (барлығын өшіру)
#print(myList)

# әдістер тізімді өзі өзгертеді
myList.extend(newList)
#print(myList)

#primerList = myList.extend(newList)
#print(primerList)

#print(myList)
#first = myList.pop(0)       # 0 - ші номерде тұрған элементті шығарады және оны өшіреді
#print(first)
#print(myList)

#######################################################################################################################
#  2 Тапсырма: 1. Келесі векторды тізімге сақтап көріңіз: [13, 46, 79, 85, 95].
#             2. векторды 1-ден: 34-ке дейін көбейтуді жүзеге асыру.
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


# for итерациялық констукциясы
cars = ['Mazda', 'Mers', 'Toyota', 'BMW']

for i in cars:
    print(i)
    print(i*3)

#######################################################################################################################
#  3 тапсырма: 2-тапсырма кодын for құрылымын пайдаланып қайта жазыңыз.
#######################################################################################################################


# 1 тапсырма
#print('1 тапсырма. Ағаштың тереңдігін енгізіңіз:')
#stars = int(input())

#for star in range(1, stars+1):
#    print(star * '*')

# 2 тапсырма
# 3 тапсырма үшін: С, С++ тілдері үшін де шығару "Pyhton сияқты әдемі".

#print('Тапсырма 2. ')
languages = ["C", "Delphi", "Python", "C++", "HTML", "Perl"]

#for language in languages:
#    if language == 'Python':
#        print('Python ең керемет')
 #   else:
#        print(language, 'Python сияқты керемет емес')

# 3 тапсырма
#print('3 тапсырма. ')
#for language in languages:
#    if language == 'Python':
#        print(language, 'ең керемет')
#    elif (language == 'C') | (language == 'C++'):
#        print(language, 'Python сияқты керемет')
#    else:
#        print(language, 'Python сияқты керемет емес')


myString = 'Hello World'
i = 0

#for character in myString:
#    if character == 'l':
#        print(character)
        # continue            # келесі итерацияны бастайтын команда
#        i = i+1
#    else:
#        print('not an L')

#print("#character:", i)

# While циклі, сіз кіріс көлемін білмеген кезде қолданылады.
i = 0

#while -5 < i < 5:
#    print(i)
#    # continue
#    # break
#    i = i-1

# Үй жұмысы: 1. Тапсырманы шешу (сабақта шешім қабылдамағандар үшін) while көмегімен.
#     2. Биіктігі үшін минималды мән 3, ал максимум 30 болатындай етіп есепті қайта жасаңыз
#        (while логикалық шарт арқылы).
#     3. Негізгі кодты алып тастағаннан кейін бағдарлама оның аяғын 2 жұлдыз болатындай қалыңдығымен аяқтайтындай етіп есепті аяқтаңыз
#        (**), тереңдігі 3 жұлдыз.