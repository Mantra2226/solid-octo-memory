# Example: Smartphone system demonstrating OOP concepts in Python

# Base class
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Private attribute (Encapsulation)

    def show_details(self):
        print(f"Smartphone: {self.brand} {self.model}")
        print(f"Battery level: {self.__battery_level}%")

    def charge(self, amount):
        if amount > 0:
            self.__battery_level = min(100, self.__battery_level + amount)
            print(f"{self.model} charged. Battery now at {self.__battery_level}%")
        else:
            print("Charge amount must be positive!")

    def use(self, hours):
        usage = hours * 10
        if usage < self.__battery_level:
            self.__battery_level -= usage
            print(f"Used {self.model} for {hours} hours. Battery now at {self.__battery_level}%")
        else:
            print("Battery too low! Please charge your phone.")

    def device_type(self):
        print("This is a standard smartphone.")


# Derived class 1
class Android(Smartphone):
    def __init__(self, brand, model, battery_level, version):
        super().__init__(brand, model, battery_level)
        self.version = version

    def device_type(self):
        print(f"This is an Android device running version {self.version} 🤖")

    def use_google_assistant(self):
        print(f"{self.model}: 'Hey Google, how can I help you?' 🎤")


# Derived class 2
class iPhone(Smartphone):
    def __init__(self, brand, model, battery_level, ios_version):
        super().__init__(brand, model, battery_level)
        self.ios_version = ios_version

    def device_type(self):
        print(f"This is an iPhone running iOS {self.ios_version} 🍎")

    def use_siri(self):
        print(f"{self.model}: 'Hey Siri, what can I do for you?' 🎙️")


# Create objects
android_phone = Android("Samsung", "Galaxy S24", 80, "Android 14")
iphone = iPhone("Apple", "iPhone 15", 90, "iOS 18")

# Demonstrate functionality
android_phone.device_type()
android_phone.show_details()
android_phone.use(3)
android_phone.charge(15)
android_phone.use_google_assistant()

print()  # Line break

iphone.device_type()
iphone.show_details()
iphone.use(2)
iphone.charge(5)
iphone.use_siri()
