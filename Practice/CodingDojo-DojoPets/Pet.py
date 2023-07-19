class Pets:
    def __init__(self, name, type, treats, health, energy) -> None:
        self.name = name
        self.type = type
        self.treats = treats
        self.health = health
        self.energy = energy
    

    def sleep(self) -> None:
        print(self.name, "Se ha dormido")


    def eat(self, user_food) -> None:
        print(self.name, "Ha comido:", user_food.pet_food)


    def play(self) -> None:
        print(self.name, "Ha rodado sobre si mismo")


    def noise(self) -> None:
        print(self.name, "Ha hecho un sonido")

class Cat(Pets):
    def __init__(self, name, type, treats, health, energy) -> None:
        super().__init__(name, type, treats, health, energy)

    def noise(self) -> None:
        print("Meow!")

class Cat(Pets):
    def __init__(self, name, treats, health, energy) -> None:
        super().__init__(name, "High quality cat", treats, health, energy)

    def noise(self) -> None:
        print("Meow!")