print("Hi, Welcome to the Bank Of Mateo!")
name = input("Please Enter your first name:")
years = int(input("Please enter the number of years you would like a loan:"))
amount = float(input("Please enter the amount for your loan, in dollars:"))


if years >= 30:
    interest_rate = 15
elif 10 <= years < 30:
    interest_rate = 10
elif 5 <= years < 10:
    interest_rate = 5
else:
    interest_rate = 2

interest_amount = amount * (interest_rate / 100)
repayment = amount + (interest_amount * years)


print (f"For you {name} we have the following deal!")
print (f"For a loan amount of ${amount} we can provide you an interest rate of {interest_rate}%")
print (f"The total, with interest, will be ${repayment}") 
