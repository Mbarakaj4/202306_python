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

if num1 > 45: # Conditional: if
    print("It's greater") # Log statement, string
else: # Conditional: else
    print("It's lower") # Log statement, string

if len(string) < 5: # Conditional: if
    print("It's a short word!") # Log statement, string
elif len(string) > 15: # Conditional: else if
    print("It's a long word!") # Log statement, string
else: # Conditional: else
    print("Just right!") # Log statement, string

for x in range(5): #For loop start, variable declaration number
    print(x) # Log statement
for x in range(2, 5): #For loop, variable declaration number, start
    print(x) # Log statement
for x in range(2, 10, 3): #For loop, variable declaration number, start increment
    print(x) # Log statement
x = 0 # Variable declaration number
while x < 5: # While loop start
    print(x) # Log statement
    x += 1 # While loop increment

pizza_toppings.pop() # List delete value
pizza_toppings.pop(1) # List delete value

print(person) # Log statement
person.pop("eye_color") # Dictionary delete value
print(person) # Log statement

for topping in pizza_toppings: # For loop start
    if topping == "Pepperoni": # Conditional: if
        continue # for loop continue
    print("After 1st if statement") # Log statement
    if topping == "Olives": # Conditional: if
        break # for loop break


def print_hello_ten_times(): # Function
    for num in range(10): # For loop start
        print("Hello") # Log statement


print_hello_ten_times() 


def print_hello_x_times(x): # Function, parameter
    for num in range(x): # For loop start
        print("Hello") # Log statement


print_hello_x_times(4) 


def print_hello_x_or_ten_times(x=10): #function, parameter, variable declaration number
    for num in range(x): # For loop start
        print("Hello") # Log statement


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

#print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # variable declaration
#fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
#print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'
