# Dictionary - use Key - Value Approach
# Students to Understand Key - Value
# How to create a dictionary
person = {
    'firstname': 'John',
    'lastname': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'salary': 5000
}

# Print the dictionary
print(person)

# Print dictionary Item, We use the key age or firstname, lastname
print(person['age'])
print(person['salary'])

# Update an item from dictionary, here we update age
person['age'] = 34

# Print dictionary again to see if age has changed
print(person)

# Add a New Key and Value
person["passport"] = "BOO78hn"
# Print dictionary again to see if passport has been added
print(person)

# Remove an item from dictionary, here we update age
del person['lastname']
# Print dictionary again to see if lastname has been removed
print(person)


