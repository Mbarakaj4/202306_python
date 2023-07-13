num1 = 42  # variable declaration, Data Types: Primitive numbers
num2 = 2.3  # variable declaration, Data Types: Primitive numbers
boolean = True  # variable declaration, Data Types: Primitive boolean
string = "Hello World"  # variable declaration, Data Types: Primitive strings
pizza_toppings = [
    "Pepperoni",
    "Sausage",
    "Jalepenos",
    "Cheese",
    "Olives",
]  # variable declaration, Data Types: Composite list (Initialize)
person = {
    "name": "John",
    "location": "Salt Lake",
    "age": 37,
    "is_balding": False,
}  # variable declaration, Data Types: Composite dictionary (Initialize)
fruit = (
    "blueberry",
    "strawberry",
    "banana",
)  # variable declaration, Data Types: Composite tuples (Initialize)
print(type(fruit)) # Log statement, type check
print(pizza_toppings[1]) #Log statement, Data Types: Composite list (Access value)
pizza_toppings.append("Mushrooms") # Data Types: Composite tuple (Add value)
print(person["name"]) #Log statement, Data Types: Composite dictionary (Access value)
person["name"] = "George" #Log statement, Data Types: Composite dictionary (Change value)
person["eye_color"] = "blue" #Log statement, Data Types: Composite dictionary (Add value)
print(fruit[2]) #Log statement, Data Types: Composite tuples (Access value}

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
while x < 5:
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop("eye_color")
print(person)

for topping in pizza_toppings:
    if topping == "Pepperoni":
        continue
    print("After 1st if statement")
    if topping == "Olives":
        break


def print_hello_ten_times():
    for num in range(10):
        print("Hello")


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print("Hello")


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print("Hello")


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
