import random

file_dates_questions_ru = open('data/dates_questions_ru.txt', 'r', encoding='utf-8')
lines_dates_questions_ru = file_dates_questions_ru.readlines()
file_dates_answers_ru = open('data/dates_answers_ru.txt', 'r', encoding='utf-8')
lines_dates_answers_ru = file_dates_answers_ru.readlines()

def main_menu():
    print("=====================================================================")
    print("  Тренажер ОГЭ по истории  ")
    print("                           ")
    print(" 1. Тема:                  ")
    print("   1. Россия               ")
    print("                           ")
    print(" 2. Формат:                ")
    print("   1. Даты                 ")
    print("                           ")
    print(" Напишите = во всех полях для выхода                         ")
    print("                           ")
    theme = input("Введите тему: ")
    format = input("Введите формат: ")
    print("=====================================================================")
    return theme+format

def ru_dates ():
    print("=====================================================================")
    que_num = random.randint(0,24)
    o = que_num
    print(lines_dates_questions_ru[o].rstrip())
    print("                           ")
    answer = input("Введите ваш ответ: ")
    print("                           ")
    print(f"Верный ответ: {lines_dates_answers_ru[o].rstrip()}")
    print("=====================================================================")

def next ():
    print("=====================================================================")
    print("1 - следующий вопрос       ")
    print("2 - перейти в меню         ")
    print("                           ")
    choice = input("Введите число: ")
    print("=====================================================================")
    return choice

def game_ru_dates ():
    ru_dates()
    c = next()
    return c

a = 0
counter = 0
while (a==0):
    counter = 0
    b = main_menu()
    if b == "11":
        c = "1"
        while (c == "1"):
            counter+=1
            print(f"Вопрос №{counter}")
            c = game_ru_dates()
    elif b == "==":
        break
