# List Comprehension
# new_list = [new_item for item in list]

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]

name = "Mytruc"

letter_list = [letter for letter in name]
print(letter_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Coditional List Comprehension
# new_list = [new_item for item in list if test]

name_list = ["Alex", "Bob", "Caitlyn"]
short_name = [name for name in name_list if len(name) < 5]
print(short_name)

long_and_cap_name = [name.upper() for name in name_list if len(name) > 5]
print(long_and_cap_name)