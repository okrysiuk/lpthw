# Игра "Санаторий золотая узда"
from sys import exit

def end(why):
    print("Closing.. %s" % why)
    exit(0)


original_sin = 0

def sin():
    global original_sin
    original_sin += 1


def first_circle():
    print("Перше коло пекла. Лімб. Нехрещені новонароджені та праведники нехристияни.")
    print("Підемо далі чи хочете залишитись тут?")
    fc_sin_count = 0
    while True:
        next = input("> ")
        if next == "y":
            if fc_sin_count == 0:
                third_circle()
            elif fc_sin_count >= 5:
                end("Гра закінчена. Ваше місце восьмий круг шоста щілина.")
            else:
                print("Ви спробували %d раз вийти, це трохи вплине на карму.." % fc_sin_count)
                second_circle()
        else:
            print("Ви серйозно вважаєте себе праведником чи безгрішним як новонароджений?..")
            fc_sin_count += 1


def second_circle():
    print("This is second circle of hell.")
    exit()


def third_circle():
    print("This is third circle of hell.")


def fourth_circle():
    print("This is fourth circle of hell.")


def fifth_circle():
    print("This is fifth circle of hell.")


def sixth_circle():
    print("This is sixth circle of hell.")


def seventh_circle():
    print("This is seventh circle of hell.")


def eighth_circle():
    print("This is eighth circle of hell.")


def nineth_circle():
    print("This is nineth circle of hell.")

    
def start():
    print("Давайте знайдемо Вам тепленький затишний куточок на одному з кіл пекла по Данте.")
    print("Зараз нас чекає невеличка екскурсія, споробуйте вибрати своє коло самостійно.")
    print("Правила дуже прості, натискати потрібно лише декілька клавіш: ")
    print("y - так, n - ні")
    print("Ходімо, мій грішний друже!!")
    circle = input('> ')
    if circle == "y":
        first_circle()
    else:
        print("\nТільки вперед мій друже, думати потрібно було раніше!!!!!!!")
        print("\n")
        start()

start()
