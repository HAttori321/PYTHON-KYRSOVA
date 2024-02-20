import random
def guess_number_game(min_num=1,max_num=50,max_attempts=10):
    secret_number=random.randint(min_num,max_num)
    print("Вгадай число між",min_num,"і",max_num)
    print("У тебе є",max_attempts,"спроб")
    attempts=0
    while attempts<max_attempts:
        guess=get_guess(min_num, max_num)
        attempts+=1
        if guess==secret_number:
            print("Вітаю!Ти вгадав число",secret_number,"з",attempts,"спробою!")
            return
        elif guess<secret_number:
            print("Спробуй більше число.")
        else:
            print("Спробуй менше число.")
    print("Ти вичерпав всі спроби.Загадане число було",secret_number)
def get_guess(min_num,max_num):
    while True:
        try:
            guess=int(input("Ваше число: "))
            if min_num<=guess<=max_num:
                return guess
            else:
                print("Будь ласка,введи число в межах від",min_num,"до",max_num)
        except ValueError:
            print("Будь ласка, введи ціле число.")
guess_number_game()