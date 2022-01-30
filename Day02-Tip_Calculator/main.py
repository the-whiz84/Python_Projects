#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? €")
tip = input("How much tip would you like to give? 10, 12 or 15 percent? ")
people = input("How many people to split the bill? ")
tip_amount = float(total_bill) * (int(tip) / 100)

bill_with_tip = float(total_bill) + float(tip_amount)

split_bill = float(bill_with_tip) / int(people) 

print(f"Each person should pay: €{split_bill:.2f}")

#Another solution
# total_bill = float(input("What was the total bill? €"))
# tip = int(input("How much tip would you like to give? 10, 12 or 15 percent? "))
# people = int(input("How many people to split the bill? "))
# #bill_with_tip = tip / 100 * total_bill + total_bill
# bill_with_tip = total_bill * (1 + tip / 100)
# bill_per_person = bill_with_tip / people
# final_amount = round(bill_per_person, 2)
# or
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount:.2f}")
# or without .2f if final_amount is made with second option
# print(f"Each person should pay: ${final_amount}")



