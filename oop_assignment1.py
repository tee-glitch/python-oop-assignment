class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."
    
    def charge(self):
        self.battery = 100
        return f"{self.brand} {self.model} is now fully charged!"
    
    def check_storage(self):
        return f"Available storage: {self.storage}GB"


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.__gpu = gpu  # private attribute (encapsulation)

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.__gpu} GPU!"

    def get_gpu(self):
        return self.__gpu


# Testing the classes
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 80)
print(phone1.make_call("0712345678"))
print(phone1.charge())
print(phone1.check_storage())

print("----")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 90, "Adreno 740")
print(gaming_phone.make_call("0798765432"))
print(gaming_phone.play_game("PUBG Mobile"))
print("GPU:", gaming_phone.get_gpu())
