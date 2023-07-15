class CuentaBancaria:
    # Array atribute for saving the accounts created
    instance = {}

    # Constructor
    def __init__(self: object, tasa_interes: float, balance: float, account_name: str):
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.account_name = account_name
        CuentaBancaria.instance[self.account_name] = {"Balance": self.balance}

    #   Methods

    # # Add the deposito method
    # def deposito(self: object, amount: float, tr_account: str) -> object:
    #     for accounts in CuentaBancaria.instance:
    #         if tr_account == accounts:
    #             CuentaBancaria.instance[accounts]["Balance"] += amount
    #             return self

    # # Add the retiro method
    # def retiro(self: object, amount: float, tr_account: str) -> object:
    #     for accounts in CuentaBancaria.instance:
    #         if tr_account == accounts.account_name:
    #             accounts.balance -= amount
    #             return self

    # # Add the mostrar_info_cuenta method
    # def mostrar_info_cuenta(self: object) -> None:
    #     print("Balance: ${}".format(self.balance))

    # Add the generar_interes method
    def generar_interes(self: object) -> object:
        if self.tasa_interes > 0:
            self.balance += self.balance * self.tasa_interes
            return self

    # # Add the mostrar_instancias method
    # @classmethod
    # def mostrar_instancias(cls: object) -> None:
    #     for cuenta in cls.instancias:
    #         cuenta.mostrar_info_cuenta()

    @classmethod
    def get_account(cls: object, search_account: str) -> str:
        for account in cls.instance:
            if search_account == account:
                return f"{account}, Balance: {cls.instance[account]['Balance']}"


class Usuario:
    usuarios_y_cuentas = {}
    # Constructor
    def __init__(self: object, name: str, email: str, nombre_cuenta: str) -> None:
        self.name = name
        self.email = email
        self.cuenta = Usuario.usuarios_y_cuentas[name] = {nombre_cuenta : CuentaBancaria(0.02, 0, nombre_cuenta)}

    #   Methods

    def mostrar_info(self: object, mostrar_cuenta: str) -> None:
        print(
            f"Nombre: {self.name}\
              \nEmail: {self.email}\
              \nCuenta: {mostrar_cuenta}, Balance: {Usuario.usuarios_y_cuentas[self.name][mostrar_cuenta].balance}"\
        )
    
    def hacer_deposito(self: object, cuenta: str, monto: float):
        Usuario.usuarios_y_cuentas[self.name][cuenta].balance += monto
        return self

    def hacer_retiro(self: object, cuenta: str, monto: float):
        Usuario.usuarios_y_cuentas[self.name][cuenta].balance -= monto
        return self
    
    def hacer_transferencia(self: object, cuenta: str, monto: float, destino: str):
        Usuario.usuarios_y_cuentas[self.name][cuenta].balance -= monto
        Usuario.usuarios_y_cuentas[destino][cuenta].balance -= monto
        return self
    
    def agregar_cuenta(self: object, nombre_ncuenta: str):
        Usuario.usuarios_y_cuentas[self.name][nombre_ncuenta] = CuentaBancaria(0.02, 0, nombre_ncuenta)

pepe = Usuario("Pepe", "pepe@example.com", "cuenta1")
pepe.hacer_deposito("cuenta1", 5_000_000)
pepe.mostrar_info("cuenta1")
pepe.agregar_cuenta("cuenta2")
pepe.hacer_deposito("cuenta2", 2_000_000)
pepe.mostrar_info("cuenta2")

amanda = Usuario('amanda','amanda@example.com','cuenta1')
amanda.hacer_deposito("cuenta1", 4_000_000)
amanda.mostrar_info("cuenta1")
amanda.agregar_cuenta("cuenta2")
amanda.hacer_deposito("cuenta2", 500_000)
amanda.mostrar_info("cuenta2")
regie = Usuario('regie','regie@gmail.com','cuenta1')
regie.hacer_deposito("cuenta1", 60_000)
regie.mostrar_info("cuenta1")
regie.agregar_cuenta("cuenta2")
regie.hacer_deposito("cuenta2", 1_500_000)
regie.mostrar_info("cuenta2")
theUnknown = Usuario('donuwu','cowdingdwojo@weabo.uwu','cuenta1')
theUnknown.hacer_deposito("cuenta1", 6_000_000)
theUnknown.mostrar_info("cuenta1")
theUnknown.agregar_cuenta("cuenta2")
theUnknown.hacer_deposito("cuenta2", 20_000_000)
theUnknown.mostrar_info("cuenta2")
