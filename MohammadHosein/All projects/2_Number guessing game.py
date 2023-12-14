input(
    "Welcome to Number guessing game! Please press (Enter) button to start the game. "
)


def game_base():
    import random

    random_number_range = int(input("Please enter the maximum range of number: "))

    computer_number = random.randrange(1, random_number_range)

    entered_number = int(input("Please enter your guess: "))

    if entered_number == computer_number:
        print("Correct!")

    while entered_number != computer_number:
        if entered_number > computer_number:
            print("False! Guess a lessser number: ")

        elif entered_number < computer_number:
            print("False! Guess a greater number: ")

        entered_number = int(input("Please enter your guess: "))

        if entered_number == computer_number:
            print("Correct!")


game_base()

# Now we have a loop of our base of game that until we guess right, does not have any end.


def start_end():
    start_or_end = input(
        "Do you want to play again? Please enter (s) to start a new game or press (Enter) button to end the game. "
    )

    while start_or_end == "s":
        game_base()

        start_or_end = input(
            "Do you want to play again? Please enter (s) to start a new game or press (Enter) button to end the game. "
        )


start_end()

# This loop let us to continue playing until whenever we want.
