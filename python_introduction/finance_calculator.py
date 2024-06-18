#Take inputs for personal finance calculator
income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))

#now we calculate the monthly savings of the user
monthly_savings = income - expense
print("Your monthly savings are $",monthly_savings)

#now we work on annual savings assuming interest is 5% per year
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",Projected_savings)
