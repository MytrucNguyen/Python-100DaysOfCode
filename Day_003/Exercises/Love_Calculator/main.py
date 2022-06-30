# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score1 = 0
score2 = 0
first_score = "true"
second_score = "love"

combined_name = name1.lower().replace(" ", "")+name2.lower().replace(" ", "")

for char in combined_name:
    if(char in first_score):
        score1+=1
    if(char in second_score):
        score2+=1

combined_score = str(score1)+str(score2)

combined_score = int(combined_score)

score = int(combined_score)

if(score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")

elif(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
