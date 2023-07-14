class Usuario:

    # Declare class attribute
    nombre_banco = "Primer Dojo Nacional"

    # Constructor
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # Add the hacer_deposito method
    def hacer_deposito(self, amount) -> object:
        self.balance_cuenta += amount
        return self

    # Add the hacer_retiro method
    def hacer_retiro(self, amount) -> object:
        self.balance_cuenta -= amount
        return self

    # Add the mostrar_balance_usuario method
    def mostrar_balance_usuario(self) -> None:
        print("Usuario: {}, Balance: ${}".format(self.name, self.balance_cuenta))
    
    # Add the transferir_dinero method
    def transferir_dinero(self, user, amount) -> None:
        self.hacer_retiro(amount)
        user.hacer_deposito(amount)

# Create 3 User instances

pepe = Usuario("pepe","pepe@example.com")
maria = Usuario("maria","maria@example.com")
rosario = Usuario("rosario","rosario@example.com")

# Make first user make 3 deposits 2 transfers and then display their balance
pepe.hacer_deposito(101).hacer_deposito(202).hacer_deposito(103)
pepe.transferir_dinero(maria,110)
pepe.transferir_dinero(rosario,110)
pepe.mostrar_balance_usuario()

# Make second user make 2 deposits 2 transfers and then display their balance
maria.hacer_deposito(409).hacer_deposito(208)
maria.transferir_dinero(rosario,200)
maria.transferir_dinero(pepe,150)
maria.mostrar_balance_usuario()

# Make third user make 1 deposits 3 transfers and then display their balance
rosario.hacer_deposito(300)
rosario.transferir_dinero(pepe,200)
rosario.transferir_dinero(maria,100)
rosario.transferir_dinero(pepe,200)
rosario.mostrar_balance_usuario()