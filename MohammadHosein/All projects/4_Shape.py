class Circle:
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def surface(self):
        circle_surface = 3.14 * (self.circle_radius**2)
        return print(f"Your circle surface is: {circle_surface}")

    def perimeter(self):
        circle_perimeter = 3.14 * 2 * self.circle_radius
        return print(f"Your circle perimeter is: {circle_perimeter}")


class Square:
    def __init__(self, square_line):
        self.square_line = square_line

    def surface(self):
        square_surface = self.square_line**2
        return print(f"Your square surface is: {square_surface}")

    def perimeter(self):
        square_peirmeter = self.square_line * 4
        return print(f"Your square perimeter is: {square_peirmeter}")


class Rectangle:
    def __init__(self, rectangle_width, rectangle_length):
        self.rectangle_width = rectangle_width
        self.rectangle_length = rectangle_length

    def surface(self):
        rectangle_surface = self.rectangle_width * self.rectangle_length
        return print(f"Your rectangle surface is: {rectangle_surface}")

    def perimeter(self):
        rectangle_perimeter = (self.rectangle_width + self.rectangle_length) * 2
        return print(f"Your rectangle perimeter is: {rectangle_perimeter}")


class Triangle:
    def __init__(self, triangle_base, triangle_height):
        self.triangle_base = triangle_base
        self.triangle_height = triangle_height

    def surface(self):
        triangle_surface = (self.triangle_base * self.triangle_height) / 2
        return print(f"Your triangle surface is: {triangle_surface}")


def program_base():
    user_shape_type = input(
        "Please enter the type of shape that you want to calculate, (Circle), (Square), (Rectangle) or (Triangle): "
    )
    user_shape_type = user_shape_type.lower()

    user_calculation_type = input(
        "Please enter the thing that you want to calculate, (Surface) or (Perimeter (not in triangle!)): "
    )
    user_calculation_type = user_calculation_type.lower()

    if "c" in user_shape_type:
        user_circle_radius = int(input("Please enter the radius of your circle: "))
        shape = Circle(user_circle_radius)

        if "s" in user_calculation_type:
            print(shape.surface())

        elif "p" in user_calculation_type:
            print(shape.perimeter())

    elif "s" in user_shape_type:
        user_square_length = int(input("Please enter the length of your square: "))
        shape = Square(user_square_length)

        if "s" in user_calculation_type:
            print(shape.surface())

        elif "p" in user_calculation_type:
            print(shape.perimeter())

    elif "r" in user_shape_type:
        obj_rect_wid = int(input("Please enter the width of your rectangle: "))
        object_triangle_height = int(
            input("Please enter the length of your rectangle: ")
        )

        shape = Rectangle(obj_rect_wid, object_triangle_height)

        if "s" in user_calculation_type:
            print(shape.surface())

        elif "p" in user_calculation_type:
            print(shape.perimeter())

    elif "t" in user_shape_type:
        object_triangle_base = int(input("Please enter the base of your rectangle: "))
        object_triangle_height = int(
            input("Please enter the height of your rectangle: ")
        )

        shape = Triangle(object_triangle_base, object_triangle_height)

        if "s" in user_calculation_type:
            print(shape.surface())

        elif "p" in user_calculation_type:
            print("Sorry! We can not calculate triangle.")


program_base()

using_program_again = input(
    "Do you want to use this program again? Please enter (u) to use again or press (Enter) on keyboard to end: "
)

while using_program_again == "u":
    program_base()
    using_program_again = input(
        "Do you want to use this program again? Please enter (u) to use again or press (Enter) on keyboard to end: "
    )
