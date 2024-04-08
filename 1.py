# Условие: Создайте класс на тему животных.
# В классе должен присутствовать инициализатор и не менее двух методов.

from Animal import Animals # Импортируем модуль

# Создаем объекты класса
Animal_Slon = Animals("Слон","слоновых","5,000 - 12,000")    # В скобках передаем конструктору параметры
Animal_Zhiraf = Animals("Жираф","жирафовых","900 - 1,200")
Animal_Zebra = Animals("Зебра","лошадиных","350")
Animal_Lev = Animals("Лев","кошачьих","180 - 220")
Animal_Nosorog = Animals("Носорог","носорогобразных","1,000 - 3,600")

print("Слон - 1 (6)\nЖираф - 2 (7)\nЗебра  - 3 (8)\nЛев  - 4 (9)\nНосорог - 5 (0)\n")
# Даём пользователю сделать выбор
a1 = int(input("Введите цифру, чтобы прочитать краткое описание по животному\n"
               "Если ввести цифру, которая в скобках, откроется дополнительная информация\n:"))
Animal_Slon.pro()
# Вызываем метод класса через определённое условие
if a1 == 1:
        Animal_Slon.hello()
elif a1 == 2:
        Animal_Zhiraf.hello()
elif a1 == 3:
        Animal_Zebra.hello()
elif a1 == 4:
        Animal_Lev.hello()
elif a1 == 5:
        Animal_Nosorog.hello()
elif a1 == 6:
        Animal_Slon.slon()
elif a1 == 7:
        Animal_Zhiraf.zhiraf()
elif a1 == 8:
        Animal_Zebra.zebra()
elif a1 == 9:
        Animal_Lev.lev()
elif a1 == 0:
        Animal_Nosorog.nosorog()