# Base class: TV
class TV:
    def __init__(self, brand, inches):
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.inches = inches
        self.onOff = False  # TV is initially off
        self.price = 0  # Optional property, can be set later

    # Method to increase the volume (if within the range of 0-100)
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume is at maximum (100).")

    # Method to decrease the volume (if within the range of 0-100)
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is at minimum (0).")

    # Method to set the channel (must be within the range of 1-50)
    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print(f"Invalid channel. The TV has only 50 channels. Stay on channel {self.channel}.")

    # Method to reset the TV (back to channel 1, volume 50)
    def reset(self):
        self.channel = 1
        self.volume = 50

    # Method to return the TV status
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Derived class: LEDTV (inherits from TV)
class LEDTV(TV):
    def __init__(self, brand, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        # Initialize the base class (TV) with brand and inches
        super().__init__(brand, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    # Method to set the viewing angle
    def set_viewing_angle(self, angle):
        self.viewing_angle = angle

    # Method to toggle the backlight
    def toggle_backlight(self):
        self.backlight = not self.backlight

    # Method to display the details of the LED TV
    def display_details(self):
        return (f"LED TV {self.brand}: {self.inches}\" screen, {self.screen_thickness} cm thick, "
                f"Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}°, "
                f"Backlight: {'On' if self.backlight else 'Off'}.")

# Derived class: PlasmaTV (inherits from TV)
class PlasmaTV(TV):
    def __init__(self, brand, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        # Initialize the base class (TV) with brand and inches
        super().__init__(brand, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    # Method to set the viewing angle
    def set_viewing_angle(self, angle):
        self.viewing_angle = angle

    # Method to toggle the backlight
    def toggle_backlight(self):
        self.backlight = not self.backlight

    # Method to display the details of the Plasma TV
    def display_details(self):
        return (f"Plasma TV {self.brand}: {self.inches}\" screen, {self.screen_thickness} cm thick, "
                f"Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}°, "
                f"Backlight: {'On' if self.backlight else 'Off'}.")

# Example usage
if __name__ == "__main__":
    # Create an LED TV
    led_tv = LEDTV("Samsung", 55, 5, 120, 50000, 120)
    led_tv.set_viewing_angle(178)
    led_tv.toggle_backlight()
    print(led_tv.display_details())

    # Create a Plasma TV
    plasma_tv = PlasmaTV("LG", 60, 8, 180, 40000, 60)
    plasma_tv.set_viewing_angle(160)
    plasma_tv.toggle_backlight()
    print(plasma_tv.display_details())

    # Create a base TV
    tv = TV("Panasonic", 42)
    print(tv.status())
    tv.increase_volume()
    tv.set_channel(10)
    print(tv.status())
    tv.reset()
    print(tv.status())