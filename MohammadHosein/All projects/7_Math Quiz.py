import random


def number_generator():
    global first_number
    first_number = random.randint(-(quiz_max_number - 1), quiz_max_number - 1)

    global seccond_number
    seccond_number = random.randint(-(quiz_max_number - 1), quiz_max_number - 1)


def program_base():
    
        print()
        quiz_level = int(input("Enter the level of quiz (1, 2, 3): "))
        # Gets an input of the quiz level

        global quiz_max_number

        if quiz_level == 1:
            quiz_max_number = 10

        elif quiz_level == 2:
            quiz_max_number = 100

        elif quiz_level == 3:
            quiz_max_number = 1000

        # Conditions for the quiz level and the max of number

        operator_list = ["+", "-", "*", "/"]
        # A list of operators

        final_score = 10

        for i in "ABCDEFGHIJ":
            number_generator()
            operator = random.choice(operator_list)

            while (
                operator == "/"
                and round(first_number / seccond_number, 1)
                != first_number / seccond_number
                or seccond_number == 0
            ):
                number_generator()

            print()
            quiz_pherase = float(
                input(f"{i}) {first_number} {operator} {seccond_number} = ")
            )

            if operator == "+":
                quiz_answer = first_number + seccond_number

            elif operator == "-":
                quiz_answer = first_number - seccond_number

            elif operator == "/":
                quiz_answer = first_number / seccond_number

            elif operator == "*":
                quiz_answer = first_number * seccond_number

            if quiz_pherase == quiz_answer:
                print("Correct!")

            elif quiz_pherase != quiz_answer:
                print("Incorrect.")

                for _ in range(2):
                    print()
                    quiz_pherase = float(
                        input(f"{i}) {first_number} {operator} {seccond_number} = ")
                    )

                    if quiz_pherase == quiz_answer:
                        print("Correct!")
                        break

                    elif quiz_pherase != quiz_answer:
                        print("Incorrect.")

                if quiz_pherase != quiz_answer:
                    print(f"The correct answer is: {quiz_answer}")
                    final_score -= 1

        print()
        print(f"Your final score in level #{quiz_level} is: {final_score} of 10")
        print()

        if final_score < 2:
            print("Realy terrible. Try to be better.")

        elif 2 < final_score < 5:
            print("That was not good, try more.")

        elif 5 > final_score < 7:
            print("Good, but can be a lot better.")

        elif 7 > final_score < 10:
            print("Realy good! But you could be a little bit better.")

        elif final_score == 10:
            print("Great! You are the best!")

        print("Good luck!")
        print()

while True:
    try:
        program_base()
        break

    except:
        print()
        print("Sorry, there is a problem and we should end the program :(")
        
        print()
        break