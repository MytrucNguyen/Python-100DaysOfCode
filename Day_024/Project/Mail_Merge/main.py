#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

from nbformat import write
os.chdir(r'C:\Users\mytru\Documents\GitHub\Python-100DaysOfCode\Day_024\Project\Mail_Merge')

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as people_invited:
    people = people_invited.readlines()
    print(people)

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    for person in people:
        stripped_person = person.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_person)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_person}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
