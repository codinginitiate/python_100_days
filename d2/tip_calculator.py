'''
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
'''
print("Welcome to the tip calculator.")
# make bill a float and remove $ if used in input
bill = float(input("What was the total bill? ").strip().replace("$", ""))
# determine tip percentage and remove % sign if used in input
tip = float(input("What percentage would you like to tip? 10, 12,15? ").strip().replace("%", ""))/100
# make sure number of people entered a whole number
num_people = int(input("How many people to split the bill? "))
# calculate the amount each person shoule pay
amount_to_pay = (bill*(tip+1)/num_people)
# print amount to py rounded to two decimal places
print(f"Each person should pay: ${amount_to_pay:.2f}")
