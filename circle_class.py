import math

class Circle:
    def __init__(self, radii_list):
        # Store the list of radii as an instance variable
        self.radii = radii_list

    # Method to calculate the area of each circle in the list
    def calculate_areas(self):
        areas = []
        for radius in self.radii:
            area = math.pi * (radius ** 2)
            areas.append(area)
        return areas

    # Method to print areas
    def print_areas(self):
        areas = self.calculate_areas()
        for i, area in enumerate(areas):
            print(f"Circle {i + 1} with radius {self.radii[i]} has area: {area:.2f}")

# From the given list in the question
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)

circle.print_areas()