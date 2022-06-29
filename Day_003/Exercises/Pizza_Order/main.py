# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
if(size == 'l' or size == "L"):
    total += 25
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 3

if(size == 'm' or size == "M"):
    total += 20
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 3

if(size == 's' or size == "S"):
    total += 15
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 2

if(extra_cheese == "Y" or extra_cheese == "y"):
    total += 1

print(f"Your final bill is: ${total}.")
