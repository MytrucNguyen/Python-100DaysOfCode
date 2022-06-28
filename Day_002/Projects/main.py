print("Welcome to the tip calculator.")
total_bill = float(input('What was the total bill? $'))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))
each_persons_bills = (total_bill+(total_bill * percentage)) / people
print(f"Eact person should pay: ${each_persons_bills:.2f}")