#Take inputs for personal finance calculator
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#now we calculate the monthly savings of the user
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}")

#now we work on annual savings assuming interest is 5% per year
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${Projected_savings}")
