import time


def total(food_input, food_number, total_price):
    food_price = float(food_menu[food_input])
    total_price = (total_price + food_price) * food_number
    print(total_price)

    # Every time you order, prints the total price that we should pay


def program_base():
    global food_menu
    food_menu = {
        "Hamburger": "2.14",
        "Cheeseburger": "2.23",
        "Pizza": "2.96",
        "Hot dog": "2.53",
        "Fries": "1.47",
        "Shrimp": "2.67",
        "Fish": "2.68",
        "Caesar salad": "1.99",
        "Season's salad": "1.66",
        "Fruit salad": "2.33",
        "Shirazi salad": "1.97",
        "Cola": "0.64",
        "Doogh": "0.79",
        "Water": "0.42",
    }

    # A dictionary of our restaurant food menu

    print()
    for i in food_menu:
        print(f"{i}: {food_menu[i]} $")

    # A line of space to our output be more readable
    # Shows the menu

    # A variable caries the total price of our order

    while True:
        
        print()
        food_input = input(
            "Please order the food (You can end the order by typing enough): "
        ).capitalize()

        # A line of space to our output be more readable
        # Gets inputs of our order
        # Capitalize the order to not to depend on how the user types (Capitalize, upper, lower)

        if food_input == "Enough":
            break

        # This condition breaks the list by typing "enough"

        elif food_input != "Enough":
            food_number = int(input("How many? "))
            
            print()
            total(food_input, food_number, 0)

        # While we do not type "enough", gets an input to enter the number of each food we order

    # A wile loop for ordering

    print()
    print("Please wait for your food:")
    print("...")

    time.sleep(5)

    print()
    print("Here's your food! ")


# An interesting effect that when we end the ordering, prints "Please wait for your food"
# Then sleeps the program for 5 secs and prints "Here's your food"


if __name__ == "__main__":
    program_base()
