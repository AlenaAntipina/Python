import math
import random
import time

# TASK 2 | SAPER
# даны размеры поля для игры в сапер и координаты мин, стоящих на этом поле. Вывести поле игры на экран.


# разница по модулю между координатами
def diff(i, j):
    return math.fabs(i - j)

# проверяет наличие мин в округе (диагональ, вертикаль, горизонталь)
def dist_dia(p1, p2, q1, q2):
    d = 0
    d1 = diff(p1, q1)
    d2 = diff(p2, q2)
    if d1 == 1 and d2 == 1 or d1 == 1 and d2 == 0 or d1 == 0 and d2 == 1:
        d = 1
    return d

# вывод поля на экран
def print_pole(pole):
    row = len(pole)
    column = len(pole[0])
    for i in range(row):
        for j in range(column):
            print(pole[i][j], end='  ')
        print()

# задание размеров поля и количества мин рандомом, возвращает размеры поля и количество мин на нем
def enter_pole(level):
# Новичок — небольшое поле 9х9 клеток с 10 минами. В углах нет мин.
# Любитель — среднее поле 16х16 клеток с 40 минами.
# Профессионал — большое минное поле 16х30 ячеек и 99 минами.
# Особый — можно настроить размер игрового поля и количество на нем мин.
    if level == 1:
        n = random.randint(5, 10)
        m = random.randint(5, 10)
        l = random.randint(9, 15)
    if level == 2:
        n = random.randint(10, 20)
        m = random.randint(10, 20)
        l = random.randint(20, 40)
    if level == 3:
        n = random.randint(20, 30)
        m = random.randint(20, 30)
        l = random.randint(40, 70)
    return n, m, l

# определение координат мин, воозвращает координаты мин на поле
def coordinates(l1, l2, number):
    coords = []
    while (1):
        if len(coords) == number:
            break
        else:
            co = []
            co.append(random.randint(0, l1-1))
            co.append(random.randint(0, l2-1))
            t = True
            for k in coords:
                if co[0] == k[0] and co[1] == k[1]:
                    t = False
                    break
            if t == True:
                coords.append([co[0], co[1]])
    coords.sort()
    return coords

# создание поля, заполнение минами, пустыми местами и цифрами
def create_pole():
    # level = int(input('Выберите уровень сложности: \n1 - легкий \n2 - средний \n3 - сложный \n'))
    level = 1
    row, column, number = enter_pole(level)
    # print(row, column, number)

    pole = [[0 for j in range(column)] for i in range(row)]
    coords = coordinates(row, column, number)
    # print(coords)

    for k in coords:
        x = k[0]
        y = k[1]
        pole[x][y] = '*'
    # print(pole)

    for i in range(row):
        for j in range(column):
            if pole[i][j] == 0:  # count miny
                for k in coords:
                    ic = k[0]
                    jc = k[1]
                    if dist_dia(i, j, ic, jc) == 1:
                        pole[i][j] += 1
                if pole[i][j] == 0:
                    pole[i][j] = '.'

    return pole, number




# игрок вводит координаты
def choice():
    x, y = (int(i) for i in input('Введите координаты: ').split())
    return x-1, y-1

# закрытое поле
def create_empty(row, col):
    user = [['_' for j in range(col)] for i in range(row)]
    return user

# сам игровой процесс
def play(user, pole, n):
    row = len(pole)
    col = len(pole[0])

    a = int(input('0 - открыть ячейку \n1 - установить флажок\n2 - снять флажок\n'))
    f_num = 0
    f_coords = []
    if a == 1:
        if count_flags(user, n) == n:
            print('Нельзя поставить больше флажков')
            print('Осталось мин:  0')
        else:
            while (1):
                x, y = choice()
                if x >= row or y >= col:
                    print('again')
                else:
                    break
            user[x][y] = 'f'
            f_num += 1
            f_coords.append([x, y])
            print('Осталось мин: ', n - count_flags(user, n))
        return 0

    elif a == 2:
        while (1):
            x, y = choice()
            if user[x][y] != 'f':
                print('again')
            else:
                break
        user[x][y] = '_'
        f_num -= 1
        print('Осталось мин: ', n - count_flags(user, n))
        return 0

    else:

        while (1):
            x, y = choice()
            if x >= row or y >= col:
                print('again')
            else:
                break

        if is_end(x, y, pole) == False:
            user = end_miny(user, pole)
            return -1

        elif pole[x][y] == '.':
            dots_in_user = []
            dots_in_user.append([x, y])
            wrong_flags = []
            user, wrong_flags = open(user, pole, x, y, dots_in_user, wrong_flags)

            print('Осталось мин: ', n - count_flags(user, n))

            if len(wrong_flags) == 0:
                return 0

            else:
                for no_flag in wrong_flags:
                    i = no_flag[0]
                    j = no_flag[1]
                    user[i][j] = 'x'
                return -1

        else:         # pole[x][y] > 0
            set_user(user, pole, x, y)
            print('Осталось мин: ', n - count_flags(user, n))
            return 0



# установить значение
def set_user(user, pole, x, y):
    user[x][y] = pole[x][y]
    return user

# количество "-" совпадает с количеством мин - открыл все поля кроме мин - выиграл, возвращает значение True
def finish(user, n):
    row = len(user)
    column = len(user[0])
    x = 0
    for i in range(row):
        for j in range(column):
            if user[i][j] == '_' or user[i][j] == 'f':
                x+=1
    if x == n:
        return True
    else:
        return False

# если попал на мину - проиграл, возвращает значение False
def is_end(x, y, pole):
    if pole[x][y] == '*':
        return False
    else:
        return True

# открыть на поле все мины в случае проигрыша
def end_miny(user, pole):
    row = len(pole)
    column = len(pole[0])
    for i in range(row):
        for j in range(column):
            if pole[i][j] != '*' and user[i][j] == 'f':
                user[i][j] = 'x'
            if pole[i][j] == '*' and user[i][j] != 'f':
                set_user(user, pole, i, j)
    return user

# открыть часть поля в округе
def open(user, pole, x, y, dots_in_user, wrong_flags):
    set_user(user, pole, x, y)
    row = len(pole)
    col = len(pole[0])

    for i in range(row):
        for j in range(col):

            if user[i][j] == '.':
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ai = i + di              # координаты точек в округе заданной точки
                        aj = j + dj

                        if 0 <= ai < row and 0 <= aj < col and pole[ai][aj] != '*':
                            if user[ai][aj] == 'f' and [ai, aj] not in wrong_flags:
                                wrong_flags.append([ai, aj])

                            set_user(user, pole, ai, aj)

                            if user[ai][aj] == '.' and [ai, aj] not in dots_in_user:
                                dots_in_user.append([ai, aj])
                                open(user, pole, ai, aj, dots_in_user, wrong_flags)

    return user, wrong_flags

# сколько флажков уже выставлено
def count_flags(user, n):
    k = 0
    for i in range(len(user)):
        for j in range(len(user[0])):
            if user[i][j] == 'f':
                k += 1
    return k

# запуск игры
def game():
    pole, n = create_pole()
    # print_pole(pole)
    # print('_______________')

    user = create_empty(len(pole), len(pole[0]))
    print(f'Размер поля:  {len(pole)}x{len(pole[0])}')
    print('Всего мин:  ', n)
    print_pole(user)

    while (1):
        if finish(user, n) == True:
            print('CONGRATULATIONS! YOU WIN')
            print_pole(user)
            break

        res = play(user, pole, n)
        if res == -1:  # попал на мину - проиграл
            print('GAME OVER')
            print_pole(user)
            break
        else:  # открыть часть поля
            print_pole(user)
            print()




# MAIN
game()





