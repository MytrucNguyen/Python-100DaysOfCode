import os
os.chdir(r"C:\Users\mytru\Documents\GitHub\Python-100DaysOfCode\Day_030\Notes\Catching_Exceptions")

#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
    # something that might cause an exception
# except:
    # do this if there was an exception
# else:
    # do this if there were no exceptions
# finally:
    # do this no matter what happens

try:
    file = open("a_file.txt")
    a_dictionary  = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")

except KeyError as error_message:
    print(f"That key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File closed")