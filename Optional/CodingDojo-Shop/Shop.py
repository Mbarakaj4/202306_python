from Product import Product


class Shop:
    """
    Atributos:
        name: str
        products: list

    Metodos:
        agregar_producto(nuevo_producto) -> None

        vender_producto(id) -> None
        
        inflacion(porcentaje_aumento) -> None
        
        hacer_liquidacion(categoria, porcentaje_descuento) -> None 
    """

    # Constructor
    def __init__(self: object, name: str, products: list) -> None:
        self.name = name
        self.products = products

    def agregar_producto(self: object, nuevo_producto: object) -> None:
        """
            Agrega un nuevo objeto producto a la lista de productos.

        """
        self.products.append(nuevo_producto)

    def vender_producto(self: object, id: int) -> None:
        """
            Elimina un producto de la lista de productos.
        """
        print(self.products[id])
        self.products.pop(id)

    def inflacion(self: object, porcentaje_aumento: float) -> None:
        """
            Aumenta el precio de todos los productos
        """
        for product in self.products:
            product.print_info()
            product.price += (product.price * porcentaje_aumento) / 100
            product.print_info()

    def hacer_liquidacion(self: object, categoria: str, porcentaje_descuento: float) -> None:
        """
            Reduce el precio de todos los productos de la categoria
        """
        for product in self.products:
            if product.category == categoria:
                product.print_info()
            product.price -= (product.price * porcentaje_descuento) / 100
            product.print_info()
