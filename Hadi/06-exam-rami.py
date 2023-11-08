import random
number1 = 0
number2 = 0
score = 0
print()
print("Welcome to the exam!")

while True:
    try:
        exam_level = int(input("First please enter the level of your exam. enter: 1 or 2 or 3 :"))
        if exam_level < 1 or exam_level > 3:
            raise ValueError
        break
    except:
        pass

def number_selection():
    global number1
    global number2
    if exam_level == 1:
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
    elif exam_level == 2:
        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
    elif exam_level == 3:
        number1 = random.randint(100,999)
        number2 = random.randint(100,999)

def question():
    global score
    response_try = 1
    print()
    while response_try < 4:
            user_answer = int(input(f"Question.{question_number}.   {number1} + {number2} = "))
            if user_answer == number1 + number2:
                score += 1
                print(f"FINE! Score up to now: {score}")
                break
            elif response_try < 3:
                response_try += 1
                print (f"Nope, Try agian! try_no({response_try}):")
            else:
                print(f"NOPE! The Answer is: {number1 + number2}. Score up to now:{score}")
                response_try += 1

print()
print("Note: You can try each question for 3 times!")

for question_number in range (1,11):
    number_selection()
    question()

print()
print("Thank you for participation.")
print(f"YOUR FINAL SCORE: {score}")
print()