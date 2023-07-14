class Usuario:

    # Declare class attribute
    nombre_banco = "Primer Dojo Nacional"

    # Constructor
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # Add the hacer_deposito method
    def hacer_deposito(self, amount) -> None:
        self.balance_cuenta += amount

    # Add the hacer_retiro method
    def hacer_retiro(self, amount) -> None:
        self.balance_cuenta -= amount

    # Add the mostrar_balance_usuario method
    def mostrar_balance_usuario(self) -> None:
        print("Usuario: {}, Balance: ${}".format(self.name, self.balance_cuenta))
    
    # Add the transferir_dinero method
    def transferir_dinero(self, user, amount) -> None:
        self.hacer_retiro(amount)
        user.hacer_deposito(amount)


# # Create instances of usuario
# guido = Usuario()
# monty = Usuario()

# # Access to instance values
# print(guido.name)
# print(monty.name)

# # Assign values to instance attributes and print
# guido.name = "Guido"
# monty.name = "Monty"
# guido.nombre_banco = "Dojo Credit Union"
# print(guido.name)
# print(monty.name)
# print(guido.nombre_banco)
# print(monty.nombre_banco)

# Pasing arguments to constructor
# guido = Usuario("Guido van Rossum", "guido@python.com")
# monty = Usuario("Monty Python", "monty@python.com")
# print(guido.name)
# print(monty.name)
# guido.hacer_deposito(100)
# guido.hacer_deposito(200)
# monty.hacer_deposito(50)
# print(guido.balance_cuenta)
# print(monty.balance_cuenta)

# Create 3 User instances

pepe = Usuario("pepe","pepe@example.com")
maria = Usuario("maria","maria@example.com")
rosario = Usuario("rosario","rosario@example.com")

# Make first user make 3 deposits 2 transfers and then display their balance
pepe.hacer_deposito(101)
pepe.hacer_deposito(202)
pepe.hacer_deposito(103)
pepe.transferir_dinero(maria,110)
pepe.transferir_dinero(rosario,110)
pepe.mostrar_balance_usuario()

# Make second user make 2 deposits 2 transfers and then display their balance
maria.hacer_deposito(409)
maria.hacer_deposito(208)
maria.transferir_dinero(rosario,200)
maria.transferir_dinero(pepe,150)
maria.mostrar_balance_usuario()

# Make third user make 1 deposits 3 transfers and then display their balance
rosario.hacer_deposito(300)
rosario.transferir_dinero(pepe,200)
rosario.transferir_dinero(maria,100)
rosario.transferir_dinero(pepe,200)
rosario.mostrar_balance_usuario()