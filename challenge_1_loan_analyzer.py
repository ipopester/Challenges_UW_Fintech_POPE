# coding: utf-8
import csv
from pathlib import Path


"""This is a Python program that automates tasks associated with valuing microlending loans. The following is included:

1. Automation of Calculations; formulas allowing automation of basic loan calculations, such as number of loans, total value, and average cost are provided.
2. Loan Data Analysis on a monthly basis:
    -> A decision as to whether the loan should be purchased based on a given discount rate is provided.
    -> The analysis can completed using either a formula or Python function for present value (fair value).
3. Conditional Filtering of Lists of Loans
    -> A Python function that allows the user to conditionally filter a dataset of lists of loans is provided.
    -> For example, the list of loans can be reduced to those that cost $500 or less
    -> The results are saved as a .csv file: the output is converted into a .csv file for storage and/or further analysis.
*Contact: iancpope@uw.edu

"""


"""

1. Automation of Calculations: formulas allowing automation of basic loan calculations, such as number of loans, total value, and average cost are provided.

"""


#List of loans:

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
number_loans = len(loan_costs)

# Print the number of loans from the list
print(f"The total number of loans is: {number_loans}")

# What is the total of all loans?
sum_loans = sum(loan_costs)

# Print the total value of the loans
print(f"The total value of the loans is: ${sum_loans: .2f}")

# What is the average loan amount from the list?
average_loan_amount = sum_loans / number_loans

# Print the average loan amount
print(f"The average loan amount is: ${average_loan_amount: .2f}")


"""

2. Loan Data Analysis on a monthly basis:
    -> A decision as to whether the loan should be purchased based on a given discount rate is provided.
    -> The analysis can completed using either a formula or Python function for present value (fair value).

"""


# Given the following loan data, you will need to calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Print each variable.
print(f"The future value is: ${future_value: .2f}.")
print(f"The number of remaining months is: {remaining_months}.")

# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate = 0.20

present_value = future_value / (1 + discount_rate / 12) ** remaining_months
print(f"The fair value of the loan is: ${round(present_value, 2)}.")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

loan_cost = loan.get("loan_price")

if present_value >= loan_cost:
    print("The loan is worth at least the cost to buy it. Go for it!")
else:
    print("The fair value of the loan is less than the cost, therfore, the loan is too expensive.")

# Given the following loan data, you will need to calculate the present value for the loan

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# This function  will be used to calculate present value.
#    This function includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function returns the `present_value` for the loan.

annual_discount_rate = 0.20


def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

# Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

present_value = calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),annual_discount_rate)


#print(f"The present value of the loan is: {present_value}")

print(f"The present value is: ${present_value: .2f}.")


"""

3. Conditional Filtering of Lists of Loans
    -> A Python function that allows the user to conditionally filter a dataset containing a list of loans is provided.
    -> For example, the list of loans can be reduced to those that cost $500 or less
    -> The results are saved as a .csv file: the output is converted into a .csv file for storage and/or further analysis.
"""


#Below is a dataset with a list of loans:

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`

inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list

for item in loans:
    if item.get("loan_price") <= 500:
        inexpensive_loans.append(item)

# Print the `inexpensive_loans` list

print(f"The inexpensive loans are: {inexpensive_loans}.")

#At this point, the output will be saved to a .csv file:
###

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(header)
    
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

