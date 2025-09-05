# In this Lesson we will Do Dta Types List, Tuples and Dictionary
# Define a List
# NB: ALways remind students that we count List items from Zero, Lists uses []
items = ['Honda', 'Nissan', 'Surf', 'Mazda', 'Volkswagon']

# Print
print(items)

# Accessing List items by index
print(items[2])

# Slicing
# Print from index 2 to 5, There is a minus one
print(items[2:6])

# Print from index 3 and above
print(items[3:])

# Print upto index 4 and below, There is a minus one
print(items[:5])

# List are mutable, Can be updated
# Lets Understand List Mutability
# Lets Update our List by Appending BMW into our List
items.append("BMW")

# Now Print Your List
print(items)  # Notice from output BMW is at Last

# Insert Toyota at a Given Position, Below we Insert Cars at Position 2
items.insert(2, "Toyota")

# Now Print Your List, Notice Toyota at Position 2
print(items)

# Next, What are Tuples? How do they Differ from Lists?