print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill_and_tip_per_person = (bill + (bill * (tip / 100))) / people

print(f"Total per person $: {total_bill_and_tip_per_person}")

