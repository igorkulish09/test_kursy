import this
print(this)

from random import randint
num = randint(1,10)
print('Привіт! Вгадай число від 1 до 10')
print(num) # для себе
x = num


num = input('Ваше число?: ')
if num.isdecimal() == False:
      print('В рядку є буква! Введіть число')
else:
     num_to_in = int(num)
     if num_to_in == x:
      print("Вітаю! Ви вгадали загадане число!")
     elif num_to_in < 1:
      print('Число не входить в ряд від 1 до 10! Спробуй ще!')
     elif num_to_in > 10:
        print('Число не входить в ряд від 1 до 10! Спробуй ще!')
     else:
        print ('Дуже близько! Спробуй ще!')
