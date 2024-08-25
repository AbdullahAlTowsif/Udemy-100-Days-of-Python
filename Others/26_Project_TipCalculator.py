print("Welcome to the tip calculator!")
bill = float(input(f"What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

ans_tip = tip/100
pay_tip = ans_tip * bill
total_bill = bill + pay_tip
each_pay = round(total_bill/people, 2)

print(f"Each person should pay: ${each_pay}")