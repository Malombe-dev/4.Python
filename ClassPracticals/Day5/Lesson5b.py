def area(base, height):
    """Calculate the area of a triangle"""
    return 0.5 * base * height

def multiple_areas():
    """Calculate areas of multiple triangles using a loop"""
    num = int(input("How many triangles do you want to calculate? "))
    for i in range(num):
        b = float(input(f"Enter base of triangle {i+1}: "))
        h = float(input(f"Enter height of triangle {i+1}: "))
        print(f"Area of triangle {i+1} is: {area(b, h)}")

# Run
multiple_areas()