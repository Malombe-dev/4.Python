try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input, please enter a number.")
else:
    print(f"Division successful {10 / num}")
finally:
    print("End of program.")
