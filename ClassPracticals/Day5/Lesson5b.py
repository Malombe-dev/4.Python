# Functions with parameters
# Functions can have Parameters

# Example 2
def great(name):
    print("Hi")
    print("Good Morning", name)


# Call Function
great("John")




# num1 and num2 are parameters
# Example 2
def add(num1, num2):
    # num1 = 20
    # num2 = 89
    answer = num1 + num2
    print('The addition is ', answer)
 

# Function call
# We provide the arguments, 90 and 4 are arguments
add(num1=90, num2=4)
# We can call the function again with different arguments, here 190 and 10 qualify to be arguments.
add(num1=190, num2=10)





# # Example 3
def bmi(weight, height):
    answer = weight/(height * height)
    print("The Body Mass Index is ", answer)


# Call Function and Provide Arguments
bmi(weight=67.7, height=1.8)

# Call smae function with different arguments
bmi(weight=80.0, height=1.9)

# We learn that with params and args, one function can be made to produce different outputs