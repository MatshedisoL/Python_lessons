# Activity 1

class Smartphone:
    def __init__(self, brand, model, storage, ram, battery_capacity):
        """
        Initialize the smartphone object with its basic specifications.
        """
        self.__brand = brand  # Encapsulated attribute
        self.__model = model  # Encapsulated attribute
        self.storage = storage  # Public attribute
        self.ram = ram  # Public attribute
        self.battery_capacity = battery_capacity  # Public attribute
        self.__power_on = False  # Encapsulated power state
        self.installed_apps = []  # List to store installed applications

    # Encapsulation: Getter for brand and model
    def get_brand_model(self):
        return f"{self.__brand} {self.__model}"

    # Encapsulation: Setter for brand and model
    def set_brand_model(self, brand, model):
        self.__brand = brand
        self.__model = model

    def turn_on(self):
        """Turn the smartphone on."""
        if not self.__power_on:
            self.__power_on = True
            print(f"{self.get_brand_model()} is now ON.")
        else:
            print(f"{self.get_brand_model()} is already ON.")

    def turn_off(self):
        """Turn the smartphone off."""
        if self.__power_on:
            self.__power_on = False
            print(f"{self.get_brand_model()} is now OFF.")
        else:
            print(f"{self.get_brand_model()} is already OFF.")

    def install_app(self, app_name):
        """Install an app on the smartphone."""
        if self.__power_on:
            if app_name not in self.installed_apps:
                self.installed_apps.append(app_name)
                print(f"App '{app_name}' installed successfully.")
            else:
                print(f"App '{app_name}' is already installed.")
        else:
            print("Cannot install apps while the phone is OFF. Please turn it ON.")

    def uninstall_app(self, app_name):
        """Uninstall an app from the smartphone."""
        if self.__power_on:
            if app_name in self.installed_apps:
                self.installed_apps.remove(app_name)
                print(f"App '{app_name}' uninstalled successfully.")
            else:
                print(f"App '{app_name}' is not installed.")
        else:
            print("Cannot uninstall apps while the phone is OFF. Please turn it ON.")

    def check_specs(self):
        """Display the specifications of the smartphone."""
        specs = f"""
        Brand: {self.__brand}
        Model: {self.__model}
        Storage: {self.storage}GB
        RAM: {self.ram}GB
        Battery: {self.battery_capacity}mAh
        """
        print(specs)

    def list_installed_apps(self):
        """List all installed apps."""
        if self.installed_apps:
            print("Installed apps:")
            for app in self.installed_apps:
                print(f"- {app}")
        else:
            print("No apps installed.")

# Subclass: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, ram, battery_capacity, gpu):
        """
        Initialize a gaming smartphone with an additional GPU attribute.
        """
        super().__init__(brand, model, storage, ram, battery_capacity)
        self.gpu = gpu  # GPU type for gaming

    # Overriding check_specs to include GPU details
    def check_specs(self):
        super().check_specs()
        print(f"GPU: {self.gpu}")

    def activate_game_mode(self):
        """Simulate activating a game mode."""
        print(f"{self.get_brand_model()}'s Game Mode activated for high performance!")

# Subclass: CameraSmartphone
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, ram, battery_capacity, camera_megapixels):
        """
        Initialize a camera smartphone with additional camera specifications.
        """
        super().__init__(brand, model, storage, ram, battery_capacity)
        self.camera_megapixels = camera_megapixels

    # Overriding check_specs to include camera details
    def check_specs(self):
        super().check_specs()
        print(f"Camera: {self.camera_megapixels} MP")

    def take_photo(self):
        """Simulate taking a photo."""
        print(f"{self.get_brand_model()} takes a stunning {self.camera_megapixels} MP photo!")

# Demonstration of Polymorphism and Encapsulation
def smartphone_demo(phone):
    phone.turn_on()
    phone.check_specs()
    if isinstance(phone, GamingSmartphone):
        phone.activate_game_mode()
    elif isinstance(phone, CameraSmartphone):
        phone.take_photo()
    phone.turn_off()

# Example Usage
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, 16, 6000, "Adreno 730")
camera_phone = CameraSmartphone("Samsung", "Galaxy S23 Ultra", 256, 12, 5000, 200)

# Demonstrate functionality
smartphone_demo(gaming_phone)
print("\n")
smartphone_demo(camera_phone)

#Activity 2

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """Abstract method to be implemented by subclasses."""
        pass

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Example Usage
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()

    # Demonstrating polymorphism
    vehicles = [car, plane, boat, bicycle]
    demonstrate_movement(vehicles)
