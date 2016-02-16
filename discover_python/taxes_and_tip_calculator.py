# Author: Electra Chong
# Program: Taxes and Tip Calculator
# Purpose: Calculate the total cost of a meal from the price fore tax, tax percentage and tipping amount. 

# Print welcome statement
print "Welcome to the taxes and tip calculator!"

# Prompt input for price
price = float(raw_input("What is the price before tax? "))

# Prompt input for tax, convert to float and divide by 100 for a decimal value
tax = float(raw_input("What are the taxes? (in %) ")) / 100

# Promopt input for tip amount, convert to float and divide by 100 for a decimal value
tip = float(raw_input("What do you want to tip? (in %) ")) / 100

# Calculate total: Multiply the price by 100% + the tax amount, then multiply taxed total by 100% + the tip amount.
total = price * (1 + tax) * (1 + tip)

# Print the total in a statement
print "The price you need to pay is: %f" % total