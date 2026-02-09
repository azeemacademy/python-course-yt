#Salary 
#Expenses: Food,Gym,Enterntaiment, Learing, Other, 
# Remaining 
# Saving : 30% Remaing
# Emergency Fund: 70% Remaning 
username=input("Enter Your Name ")
salary=int(input("Entery Your Monthly Selary: "))
food_exp=int(input("Entery Your Daily Food Exp: "))
monthly_food_exp=food_exp*30 # Month Food Expe
gym_exp=int(input("Enter Your Gym Exp: "))
entertainment_exp=int(input("Enter Your Montlhy Entertainment Exp: "))
learing_exp=int(input("Enter Your Learing Exp: "))
other_exp=int(input("Enter your other Exp: "))

#Total Exps
total_exp=monthly_food_exp+gym_exp+entertainment_exp+learing_exp+other_exp
# Remaning Amount
remaing_amount=salary-total_exp

#remaing_amount*30/100 = 30%

# Find 30% Of remaing_amount
saving=int(remaing_amount*30/100)

# Emergency Fund
emergency_fund=int(remaing_amount-saving)

#Message
print(f"Hi {username} your monthy salary is {salary}. And your monthly Expense are {total_exp} and your remaing amount is {remaing_amount}. And you can save 30%:  {saving} and your emergency fund is {emergency_fund}")