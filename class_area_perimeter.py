class Circle:
    # Private member variable for the value of pi
    _pi = 3.14

    def __init__(self, radii_list):
        # Store the list of radii as an instance variable
        self.radii = radii_list

    @classmethod
    def area(cls, radius):
        # Area = pi * r^2
        return cls._pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        # Perimeter = 2 * pi * r
        return 2 * cls._pi * radius

    def calculate_areas(self):
        areas = [self.area(radius) for radius in self.radii]
        return areas

    def calculate_perimeters(self):
        perimeters = [self.perimeter(radius) for radius in self.radii]
        return perimeters

    def print_areas_and_perimeters(self):
        areas = self.calculate_areas()
        perimeters = self.calculate_perimeters()

        for i, radius in enumerate(self.radii):
            print(f"Circle {i + 1} with radius {radius} has area: {areas[i]:.2f} and perimeter: {perimeters[i]:.2f}")


# From the given list in the question
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)

circle.print_areas_and_perimeters()