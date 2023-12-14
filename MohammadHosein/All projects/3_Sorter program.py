def number_sorting():
    number_of_number = int(
        input("Please enter the number of numbers that you want to sort: ")
    )

    main_list = [
        int(input("Please enter your number #%d: " % i))
        for i in range(1, number_of_number + 1)
    ]

    # We have a loop for getting inputs of numbers from user to sort that saves in a list.

    type_of_sort = str(
        input(
            "Please enter the type of sort, (a) for ascending or (d) for descending: "
        )
    )
    type_of_sort = type_of_sort.lower()

    # We have an input to get the Reverse of the sort.
    # No problem with forgetting to turn the Caps Lock off.

    if type_of_sort == "a":
        type_of_sort = False

    elif type_of_sort == "d":
        type_of_sort = True

    # Conditions for Reverse determination.

    sorted_list = sorted(main_list, reverse=type_of_sort)

    sorted_list = str(sorted_list)
    sorted_list = sorted_list[1:-1]

    print(f"The sorted list is: {sorted_list}")

    # Prints the sorted list of numbers.


# A function for sorting the numbers.


def word_sorting():
    nummber_of_word = int(
        input("Please enter the number of words that you want to sort: ")
    )

    main_list = [
        str(input("Please enter your word #%d: " % j))
        for j in range(1, nummber_of_word + 1)
    ]

    # We have a loop for getting inputs of words from user to sort that saves in a list.

    type_of_sort = str(
        input(
            "Please enter the type of sort, (a) for ascending or (d) for descending: "
        )
    )
    type_of_sort = type_of_sort.lower()

    # We have an input to get the Reverse of the sort.
    # No problem with forgetting to turn the Caps Lock off.

    sort_key = str(
        input(
            "Do you want to sort your words by their length? If you do enter (l) or skip this option by entering (s): "
        )
    )
    sort_key = sort_key.lower()

    # We have an input to get the Key of the sort.
    # No problem with forgetting to turn the Caps Lock off.

    if type_of_sort == "a":
        type_of_sort = False

    elif type_of_sort == "d":
        type_of_sort = True

    # Conditions for Reverse determination.

    if sort_key == "l":
        sort_key = len

    elif sort_key == "s":
        sort_key = None

    # Conditions for Key determination.

    sorted_list = sorted(main_list, key=sort_key, reverse=type_of_sort)

    sorted_list = str(sorted_list)
    sorted_list = sorted_list[1:-1]

    print(f"The sorted list is: {sorted_list}")

    # Prints the sorted list of words.


# A function for sorting the words.

input(
    "Welcome to the Sorter Program. Please press Enter on keyboard to use this program. "
)

# A welcome sentence with input() method to start the program with pressing Enter button.


def program_base():
    sort_object_type = str(
        input(
            "Please enter the type of object that you want to sort, (w) for words or (n) for numbers: "
        )
    )
    sort_object_type = sort_object_type.lower()

    # We have an input to get the sort object type.
    # No problem with forgetting to turn the Caps Lock off.

    if sort_object_type == "n":
        number_sorting()

    if sort_object_type == "w":
        word_sorting()

    # Conditions for sort object type determination.


# A function of program base.

program_base()


def use():
    use_again = str(
        input(
            "Do you want to use this program again? If you do, enter (u) or press Enter button to end the program: "
        )
    )
    use_again = use_again.lower()

    # We have an input to use the program again.
    # No problem with forgetting to turn the Caps Lock off.

    while use_again == "u":
        program_base()
        use_again = str(
            input(
                "Do you want to use this program again? If you do, enter (u) or press Enter button to end the program: "
            )
        )

    # We have a loop for using the program again.


use()
