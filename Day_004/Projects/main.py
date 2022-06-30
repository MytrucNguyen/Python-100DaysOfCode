import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = input("Rock, Paper, or Scissor? R|P|S ").lower()
print("Your Choice")
if user_input == "r":
    print(rock)
elif user_input == "p":
    print(paper)
elif user_input == "s":
    print(scissors)
else:
    print("Invalid Choice")

computer_choice = random.randint(0, 2)
print("Computer Chooses")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == 0 and user_input == "r":
    print("Draw")
elif computer_choice == 1 and user_input == "r":
    print("Computer Wins!")
elif computer_choice == 2 and user_input == "r":
    print("User Wins!")


elif computer_choice == 0 and user_input == "s":
    print("Computer Wins!")
elif computer_choice == 1 and user_input == "s":
    print("User Wins!")
elif computer_choice == 2 and user_input == "s":
    print("Draw")

elif computer_choice == 0 and user_input == "p":
    print("User Wins!")
elif computer_choice == 1 and user_input == "p":
    print("Draw")
elif computer_choice == 2 and user_input == "p":
    print("Computer Wins!")
else:
    print("Uh-Oh. You didn't choose anything.")