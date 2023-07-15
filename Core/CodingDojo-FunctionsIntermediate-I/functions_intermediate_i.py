"""
Functions Intermediate I:
1. Update values in dictionaries and lists.
    - Make a function that changes the values in a dictionary:
        - Change te value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
        - Change the last_name of the first student from 'Jordan' to 'Bryant'
        - In the directorio_deportes, change 'Messi' to 'Andres'
        - Change the value 20 in z to 30

2. Iterate through a list of dictionaries
    - Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
      the function loops through each dictionary in the list and prints each key and the associated value.

3. Find the values of a list of dictionaries
    - Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
      the function prints the value stored in that key for each dictionary.

4. Iterate through a dictionary with list values
    - Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
      prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
"""


# 1. Update values in dictionaries and lists.
def update_values() -> None:
    x = [[5, 2, 3], [10, 8, 9]]
    estudiantes = [
        {"first_name": "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
    ]
    directorio_deportes = {
        "basketball": ["Kobe", "Jordan", "James", "Curry"],
        "futbol": ["Messi", "Ronaldo", "Rooney"],
    }
    z = [{"x": 10, "y": 20}]

    x[1][0] = 15
    estudiantes[0]["last_name"] = "Bryant"
    directorio_deportes["futbol"][0] = "Andres"
    z[0]["y"] = 30

    print(x)
    print(estudiantes)
    print(directorio_deportes)
    print(z)

# 2. Iterate through a list of dictionaries
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(some_list) -> None:
    for i in some_list:
        output = ""
        for key, value in i.items():
            output += '{} - {}'.format(key, value)
        print(output)

# 3. Find the values of a list of dictionaries
def iterate_dictionary2(key_name, some_list) -> None:
    for i in some_list:
        print(i[key_name])

# 4. Iterate through a dictionary with list values
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(some_dict) -> None:
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for i in value:
            print(i)

update_values()
iterate_dictionary(estudiantes)
iterate_dictionary2("first_name", estudiantes)
iterate_dictionary2("last_name", estudiantes)
print_info(dojo)