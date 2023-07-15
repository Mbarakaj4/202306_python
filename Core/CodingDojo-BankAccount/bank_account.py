# class CuentaBancaria:
# # atributo de clase
#     nombre_banco = "Primer Dojo Nacional"
#     todas_las_cuentas = []
#     def __init__(self, int_rate,balance):
#         self.tasa_int = int_rate
#         self.balance = balance
#         CuentaBancaria.todas_las_cuentas.append(self)

#     def re_tiro(self,amount):
#         # podemos usar el método estático aquí para evaluar
#         # si podemos retirar los fondos sin quedar con balance negativo
#         if CuentaBancaria.puede_retirar(self.balance,amount):
#             self.balance -= amount
#         else:
#             print("Fondos insuficientes")
#         return self    
    
#     # los métodos estáticos no tienen acceso a ningún atributo
#     # solo a lo que se le pasa
#     @staticmethod
#     def puede_retirar(balance,amount):
#     	if (balance - amount) < 0:
#             return False
#         else:
#             return True

#     # método de clase para cambiar el nombre del banco
#     @classmethod
#     def cambiar_nombre_banco(cls,name):
#         cls.nombre_banco = name

#     # método de clase para obtener balance de todas las cuentas
#     @classmethod
#     def todos_los_balances(cls):
#         sum = 0
#         # utilizamos cls para referirnos a la clase 
#         for cuenta in cls.todas_las_cuentas:
#             sum += cuenta.balance
# Me gusta escribir en spanish and english, no lo dije antes pero that's because i want to learn how to think
# in english for better code interpretation and readability
class CuentaBancaria:
    cuentas = []

    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario

    
    # Add the deposito method
    def deposito(self, amount) -> object:
        self.balance += amount
        return self

    # Add the retiro method
    def retiro(self, amount) -> object:
        self.balance -= amount
        return self

    # Add the mostrar_info_cuenta method
    def mostrar_info_cuenta(self) -> None:
        print("Balance: ${}".format(self.balance))
    
    # Add the generar_interes method
    def generar_interes(self):
       if self.tasa_interes > 0:
           self.balance += (self.balance * self.tasa_interes)
           return self
    
    # Add the mostrar_instancias method
    @classmethod
    def mostrar_instancias(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

# Create 2 intances of CuentaBancaria
cuenta1 = CuentaBancaria(0.02, 100)
cuenta2 = CuentaBancaria(0.02, 200)

# For the first account, we call the deposito 3 times, retiro 1 time, then generar_interes and 
# then mostrar_info_cuenta all in one line of code (contatenated)
cuenta1.deposito(100).deposito(100).deposito(100).retiro(50).generar_interes().mostrar_info_cuenta()

# For the second account, we call the deposito 2 times, retiro 4 times, then generar_interes and 
# then mostrar_info_cuenta all in one line of code (contatenated)
cuenta2.deposito(100).deposito(100).retiro(5).retiro(5).retiro(5).retiro(5).generar_interes().mostrar_info_cuenta()

CuentaBancaria.mostrar_instancias()