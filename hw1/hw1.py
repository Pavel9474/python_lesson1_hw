# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение
# day=int(input('Введите номер дня недели '))
# print(day)
# if day==1:
#     print('Понедельник')
# elif day==2:
#     print('Вторник')
# elif day==3:
#     print('Среда')
# elif day==4:
#     print('Четверг')
# elif day==5:
#     print('Пятница')
# elif day==6:
#     print('Суббота')
# elif day==7:
#     print('Воскресенье')
# else:
#     print('Нет такого дня')
    
# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))
x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))
distance=a = ((x2-x1)**2+(y2-y1)**2)**0.5
print(distance)