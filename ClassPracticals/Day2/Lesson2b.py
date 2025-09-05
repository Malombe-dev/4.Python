# Recap on Lists done in Previous File
# Define a tuple.
# NB: ALways remind students that we count List items from Zero, Lists uses ()
counties = ('Embu', 'Kajiado', 'Nairobi', 'Nakuru', 'Bomet','Mombasa')

# Print
print(counties)

# Accessing tuple items by index
print(counties[2])

# Slicing
# Print from index 2 to 5, There is a minus one
print(counties[2:6])

# Print from index 3 and above
print(counties[3:])

# Print upto index 4 and below, There is a minus one
print(counties[:5])

# Tuples are immutable, Cannot be updated
# Lets Try updating a tuple!
counties.append("Embu") # Run, It produces an Error!
# AttributeError: 'tuple' object has no attribute 'append

# In conclusion, List can be updated(mutable), Tuple cannot be updated(immutable).




