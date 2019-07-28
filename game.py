# -*- coding: utf-8 -*-
import sys
import codecs
import locale
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
import codecs, sys, time, random
#Не реализованная фича. Изначально планировалось предоставить пользователю ввести предпочитаемую скорость вывода текста самому.
#set1 = raw_input(u'Введите желаемую скорость отображения текста >')

def print_slow(str): #Функция, которая выводит текст с задержкой, по буквам.
    for letter in str.read():
        sys.stdout.write(letter)
        time.sleep(float(.01))

def center_house():
    step1 = codecs.open('scenario/s_center', 'r', 'utf-8')
    print_slow(step1)

def right_house():
    step2 = codecs.open('scenario/s_right', 'r', 'utf-8')
    print_slow(step2)

def left_house():
    step3 = codecs.open('scenario/s-left', 'r', 'utf-8')
    print_slow(step3)
    print u'\n 1 - РАССПРОСИТЬ АРТЁМКУ О ЖИЗНИ\n 2 - ВОСПОЛЬЗОВАТЬСЯ ПОМОЩЬЮ КЕНТА\n'
    move1 = raw_input('> ')
    if move1 == '1':
        talk()
    elif move1 == '2':
        kent()
    else:
        print u'Ебать, твой путь оборвался как-то странно, давай по новой.'
        
def kent():
    step4_1 = codecs.open('scenario/kent', 'r', 'utf-8')
    print_slow(step4_1)
    print u'\n 1 - РАССПРОСИТЬ АРТЁМКУ О ЖИЗНИ\n 2 - ПРИГРОЗИТЬ АРТЁМКЕ ПИСТОЛЕТОМ\n 3 - ПОЙТИ ДОМОЙ\n'
    move2_1 = raw_input('> ')
    if move2_1 == '1':
        talk()
    elif move2_1 == '2':
        ugroza()
    elif move2_1 == '3':
        home()
    else:
        print u'Ебать, твой путь оборвался как-то странно, давай по новой.'

def ugroza():
    step5_1 = codecs.open('scenario/ugroza', 'r', 'utf-8')
    print_slow(step5_1)

def home():
    step5_2 = codecs.open('scenario/home', 'r', 'utf-8')
    print_slow(step5_2)

def talk():
    step4_2 = codecs.open('scenario/talk', 'r', 'utf-8')
    print_slow(step4_2)
    print u'\n 1 - ПОЙТИ НА СТРЕЛУ\n 2 - ВЗЯТЬ БИЛЕТ\n 3 - ОБМЕН: пистолет на билет'
    move2_2 = raw_input('> ')
    if move2_2 == '1':
        strela()
    elif move2_2 == '2':
        take()
    elif move2_2 == '3':
        trade()
    else:
        print u'Ебать, твой путь оборвался как-то странно, давай по новой.'

def strela():
    step6_1 = codecs.open('scenario/strela', 'r', 'utf-8')
    print_slow(step6_1)

def take():
    step6_2 = codecs.open('scenario/take', 'r', 'utf-8')
    print_slow(step6_2)
    

def trade():
    step6_3 = codecs.open('scenario/trade', 'r', 'utf-8')
    print_slow(step6_3)
        
def start():
    step0 = codecs.open('scenario/s', 'r', 'utf-8')
    print_slow(step0)
    print u'\n 1 - ЦЕНТРАЛЬНАЯ ХАТА\n 2 - ПРАВАЯ ХАТА \n 3 - ЛЕВАЯ ХАТА \n'
    move0 = raw_input('> ')
    if move0 == '1':
        print u'Двигаемся к центральной хате...'
        center_house()
    elif move0 == '2':
        print u'Двигаемся в сторону правой хаты...'
        right_house()
    elif move0 == '3':
        print u'Двигаемся по направлению к левой хате...'
        left_house()
    else:
        print u'Ебать, твой путь оборвался как-то странно, давай по новой.'

start()

