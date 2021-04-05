from random import randint


def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("what number did we guess"))

        if user_guess == randint:
            print(f"you found the number({random_int}).Congratulations")
            break
        if user_guess < random_int:
            print("your number is less than the number we guessed")
            continue
        if user_guess > random_int:
            print("your number is more than the number we guessed")
            continue


if __name__ == '__main__':
    play()
