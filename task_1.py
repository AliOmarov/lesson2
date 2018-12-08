print('Введите ниже свой возраст:')

def get_age(user_age):

    try:
        a = int(user_age)

        if a > 0 and a <=3:
            print('Вероятно, вы ещё нигде не учитесь')
        elif a > 3 and a <= 6:
            print('Вероятно, вы учитесь в детском саду')
        elif a > 6 and a <= 16:
            print('Вероятно, вы учитесь в школе')
        elif a > 16 and a <= 21:
            print('Вероятно, вы учитесть в ВУЗе')
        elif a > 21 and a <= 70:
            print('Вероятно, вы работаете')
        elif a > 70 and a <= 120:
            print('Скорее всего вы уже на пенсии')
        elif a <= 0:
            print('Введите корректный возраст:')
            user_age = input()
            get_age(user_age)
        elif a > 120:
            print('Введите корректный возраст:')
            user_age = input()
            get_age(user_age)
    except ValueError: 
        print('Введите корректный возраст:')
        first_getting_age()


def first_getting_age():
    user_age = input()
    get_age(user_age)

first_getting_age()