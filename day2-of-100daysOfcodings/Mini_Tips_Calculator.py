print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?:"))
tips = int(input("How much tips would you like to give? 10, 12, 15?: "))
people = int(input("How many people to split the bill?: "))
tip_as_precent = tips / 100
total_tip_amount = total_bill * tip_as_precent
total_bill = total_bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}") 
