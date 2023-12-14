print()
file_name = input("Please enter your file's name: ")


def program_base(file):
    with open(file, "r") as file:
        lines = file.readlines()
        counter = 0

        for i in lines:
            counter += 1

            if i == "\n":
                counter -= 1

            elif i[0] == "#":
                counter -= 1
    print()
    print()
    print(f"The number of your file's line is: {counter}")


if __name__ == "__main__":
    while True:
        try:
            program_base(file_name)
            break

        except FileNotFoundError:
            print()
            print(f"Sorry, we can not find your file with name '{file_name}'")
            print(
                "If you are certain that you have entered the right name for yor file, try => 'file_name.suffix'"
            )
            break

    print()

    input("Please rate us (1 to 5): ")
    print()

    print("Thank you for your rating")
    print("We will try to get better  :)")

    print()
