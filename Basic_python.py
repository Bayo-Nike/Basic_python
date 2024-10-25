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


 # Calculating simple interest: Write a program to take the principal, rate, and time as inputs and calculate simple interest
principal = float(input("Enter principal: ")) # Initial amount
rate =float(input("Enter rate: ")) # 5% interest
time = float(input("Enter years: ")) # in years
interest = principal * rate * time
print("Interest after a given years:", interest) # Output: Interest after 2 years: 500.0


# Boolean Example: Create a program to check if a user has sufficient funds to withdraw a specified amount
# Check if the user qualifies for a loan
has_good_credit = True
has_sufficient_income = True
qualifies_for_loan = has_good_credit and has_sufficient_income
print("Qualifies for loan:", qualifies_for_loan) # Output: Qualifies for loan: True


# Arithmetic Operation:
 # Calculating monthly payment for a loan
principal = 10000
rate = 0.05 # 5% annual interest
term = 12 # 12 months
monthly_payment = (principal * rate) / term
print("Monthly payment:", round(monthly_payment)) # Output: Monthly payment: 41.666666666666664

#Conditional
balance = 300
if balance < 500:
    fee = 20
elif balance < 1000:
    fee = 10
else:
    fee = 5
print(f"Monthly fee: ${fee}")

# Loop

balances = [1000, 2500, 1500, 3500]
total_deposit = 0
for balance in balances:
    print("Iteration ",balance)
    total_deposit += balance
     
print("Total deposit for all accounts:", total_deposit)