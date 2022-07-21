import os

from nbformat import write
os.chdir(r'C:\Users\mytru\Documents\GitHub\Python-100DaysOfCode\Day_024\Note\Open_Read_and_Write')

def main():
    with open("my_file.txt", "r") as file: 
        content = file.read()
        print(content)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
main()

# Overides everything in txt file
with open("my_file.txt", "w") as file: 
    file.write("Goodbye")

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
main()

# Adds to txt file
with open("my_file.txt", "a") as file:
    file.write("!!")

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
main()

# Adding new file if it doesnt exist
with open("new_file.txt", "w") as file:
    file.write("New File")

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
main()
