class Ninja:
    def __init__(self, name, lastname, treats, pet_food, pet) -> None:
        self.name = name
        self.lastname = lastname
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def walk(self) -> None:
        print(self.pet.name, "Ha salido a pasear")


    def feed(self) -> None:
        print(self.pet.name, "Ha sido alimentado")


    def shower(self) -> None:
        print(self.pet.name, "Se ha duchado")