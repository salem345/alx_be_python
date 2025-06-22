Monthly_Income = int(input("Enter your monthly income: "))
Monthly_Expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings = Monthly_Income - Monthly_Expenses
print("Your monthly savings are","$",Monthly_Savings,".")
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: ","$",Projected_Savings,".")