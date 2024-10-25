def greet_customer():
    print("Welcome to the bank!")
# greet_customer()

 # Import necessary module
import math
 # Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius ** 2
# Main function to run the program
def main():
 # Input: radius of the circle
    radius = float(input("Enter the radius of the circle: "))
 # Calculate area
    area = calculate_area(radius)
 # Output the result
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
 # Ensure the script is run directly
if __name__ == "__main__":
    main()