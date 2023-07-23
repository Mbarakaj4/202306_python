class Product:
    """ 
    Atributos:
        name: str
        price: float
        category: str
    
    Métodos:
        actualizar_precio(cambio_porcentaje, esta_elevado) -> None
        
        print_info() -> None 
    """
    
    # Constructor
    def __init__(self: object, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category

    def actualizar_precio(self, cambio_porcentaje, esta_elevado) -> None:
        """ Si <esta_elevado> es True, el precio se incrementa en cambio_porcentaje,
        si es False, se decrementa en cambio_porcentaje """
        if esta_elevado:
            self.price += (self.price * cambio_porcentaje) / 100
        else:
            self.price -= (self.price * cambio_porcentaje) / 100

    def print_info(self) -> None:
        """ Imprime los atributos del objeto """
        print(self.name, self.price, self.category)
