"""
    Shop and products
    Create a shop class that will have 2 attributes; a name and a list
    of products, this will start empty.

    Then create a product class that will have 3 attributes; name price
    and a category
""" 
import Shop
import Product

apple = Product.Product("Apple", 1.99, "Fruit")
banana = Product.Product("Banana", 0.99, "Fruit")
orange = Product.Product("Orange", 0.99, "Fruit")
tangerine = Product.Product("Tangerine", 0.99, "Fruit")
milk = Product.Product("Milk", 1.99, "Dairy")
cheese = Product.Product("Cheese", 1.99, "Dairy")


GoodStore = Shop.Shop("Good Store", [apple, banana, orange, tangerine,
                                      milk])

GoodStore.agregar_producto(cheese)
GoodStore.inflacion(10)
GoodStore.hacer_liquidacion("Fruit",10)
