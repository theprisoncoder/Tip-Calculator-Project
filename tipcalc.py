
import math

print("Welcome to Brendan's tip calculator!")
bill = float(input("What is the total bill? "))
tip = int(input("How much tip would you like to give? 10, 20, or any percentage? "))
people = int(input("How many people will be splitting the bill? "))

# A Night To Remember
# Calculations for spliting a bill of 25,000,000 between 3 people
# tipPercentage = tip% of bill = 31% of 25,000,000.00 = 7,750,000.00

# billAndTip = bill + tipPercentage = 25,000,000 + 7,750,000 = 32,750,000

# pitchIn = total bill / people = 32,750,000 / 3 = 10,916,666.67

tipPercentage = (tip/100)* bill
billAndTip = bill + tipPercentage
pitchIn = round(billAndTip/people, 2)

#:.2f works with the f-string to round the tipPercentage to the nearest 2 decimal places to represent cents
print(f"Your final bill includes a 10% sales tax. Receipt is as follows: \n\tFood bill {bill}, \n\tTip {tipPercentage:.2f}, \n\t$ pitched in {pitchIn:.2f}, \n\tTotal bill {billAndTip:.2f}")
print("Thank you! Come again!")