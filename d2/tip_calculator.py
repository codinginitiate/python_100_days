'''
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
'''
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? ").strip().replace("$", ""))
tip = float(input("What percentage would you like to tip? 10, 12,15? "))/100
num_people = int(input("How many people to split the bill? "))
amount_to_pay = round((bill*(tip+1)/num_people),2)
print(f"Each person should pay: ${amount_to_pay}")
